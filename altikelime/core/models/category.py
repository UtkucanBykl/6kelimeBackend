from django.db import models

from ..models import BaseModel

__all__ = ['Category']


class Category(BaseModel):
    name = models.CharField('Ad', max_length=140)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name
