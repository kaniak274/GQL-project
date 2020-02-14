from django.contrib.auth import get_user_model
from django.http import Http404
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
        if not info.context.user.is_authenticated:
            return None
        else:
            return Note.objects.select_related('user').filter(user=info.context.user)

    def resolve_users(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return None

        return get_user_model().objects.all()

    def resolve_note(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return None

        id = kwargs.get('id')

        if not id:
            return None

        note = get_object_or_404(Note, id=id)

        if note.user != info.context.user:
            raise Http404

        return note


class NoteMutation(DjangoModelFormMutation):
    note = graphene.Field(NoteType)

    class Meta:
        form_class = NoteForm


class Mutation(object):
    add_note = NoteMutation.Field()
