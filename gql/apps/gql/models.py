from django.contrib.auth import get_user_model
from django.db import models

from model_utils.models import TimeStampedModel


class Note(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notes', null=True, blank=True)

