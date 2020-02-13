import graphene

from graphene_django.types import DjangoObjectType

from .models import Note


class NoteType(DjangoObjectType):
    class Meta:
        model = Note


class Query(object):
    notes = graphene.List(NoteType)

    def resolve_notes(self, info, **kwargs):
        return Note.objects.select_related('user').all()
