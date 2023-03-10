from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth import get_user_model

from api import serializers
from things.models import Thing


class ThingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for `Thing` model.
    """
    queryset = Thing.objects.all()
    serializer_class = serializers.ThingSerializer

    def get_queryset(self):
        """
        `get_queryset()` is defined here so we can use debugger to spy on `self`.
        """
        print()
        print('self.get_view_name(): ', self.get_view_name())
        return super().get_queryset()


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for `User` model.
    """
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


# Optional parent classes:
# * `viewsets.ReadOnlyModelViewSet` - Allows `GET` requests only.
# * `viewsets.ModelViewSet` - Allows `POST`, `PUT`, `PATCH`, `DELETE` requests.
class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Get all `users` then use `filter` on that queryset to get the current user queryset.
    """
    # Get all `users`:
    queryset = get_user_model().objects.all()
    serializer_class = serializers.CurrentUserSerializer

    def get_queryset(self):
        """
        Filter the class's queryset to get the current user queryset.
        """
        print()
        # `self.get_view_name()` returns `Current User List` from `CurrentUserViewSet`:
        print('self.get_view_name(): ', self.get_view_name())
        # Filter the class's queryset to get the current user queryset:
        return self.queryset.filter(id=self.request.user.id)
