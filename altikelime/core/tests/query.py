from django.test import TestCase

from ..models import Category


class QueryTestCase(TestCase):

    def test_get_post_activies(self):
        Category.objects.create(status='OPEN', name='Cat1')
        Category.objects.create(status='CLOSE', name='Cat2')
        self.assertEquals(Category.objects.filter(status='OPEN').count(), Category.objects.actives().count())
