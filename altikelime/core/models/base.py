from django.db import models
from ..constants import STATUS, OPEN

__all__ = ['BaseModel']


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default=OPEN, max_length=10)

    class Meta:
        abstract = True
