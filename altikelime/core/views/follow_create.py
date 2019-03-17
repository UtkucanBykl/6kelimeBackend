from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Follow

__all__ = ['FollowCreateAPIView']


class FollowCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Follow.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            following = User.objects.get(username=request.data['following'])
        except User.DoesNotExist:
            return Response({'status': 'Böyle Bir kullanıcı Yok'}, status=status.HTTP_404_NOT_FOUND)
        follower = self.request.user
        qs = self.get_queryset()
        if qs.filter(following=following, follower=follower).exists():
            qs.filter(following=following, follower=follower).delete()
            return Response({'status': 'deleted'}, status=status.HTTP_201_CREATED)
        else:
            Follow.objects.create(following=following, follower=follower)
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)
