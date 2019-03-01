from django.db import models
from ..constants import STATUS, OPEN, INSPECTING

__all__ = ['BaseModel', 'BaseModelQuerySet']


class BaseModelQuerySet(models.QuerySet):
    """
    .actives() return STATUS OPEN
    .INSPECTING() return STATUS INSPECTING
    """

    def actives(self):
        return self.filter(status=OPEN)

    def inspecting(self):
        return self.filter(status=INSPECTING)


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default=OPEN, max_length=10)

    objects = BaseModelQuerySet.as_manager()

    class Meta:
        abstract = True
