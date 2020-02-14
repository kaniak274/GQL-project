from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

import graphene

from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django.types import DjangoObjectType

from .forms import NoteForm
from .models import Note


class NoteType(DjangoObjectType):
    class Meta:
        model = Note


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(object):
    notes = graphene.List(NoteType)
    users = graphene.List(UserType)

    note = graphene.Field(NoteType, id=graphene.Int())

    def resolve_notes(self, info, **kwargs):
        return Note.objects.select_related('user').all()

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_note(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return get_object_or_404(Note, id=id)

        return None


class NoteMutation(DjangoModelFormMutation):
    note = graphene.Field(NoteType)

    class Meta:
        form_class = NoteForm


class Mutation(object):
    add_note = NoteMutation.Field()
