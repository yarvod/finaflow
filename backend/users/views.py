from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from authentication.authenticate import CustomAuthentication
from users.models import User
from users.serializers import UserWRITESerializer, UserREADSerializer


class UserDefaultPagination(LimitOffsetPagination):
    default_limit = 9
    max_limit = 18


class UserMeView(ModelViewSet):
    http_method_names = ["get", "post", "put"]
    queryset = User.objects.all()
    authentication_classes = (CustomAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = UserDefaultPagination

    def get_object(self):
        if len(self.kwargs) != 0:
            return get_object_or_404(self.queryset, **self.kwargs)
        else:
            return User.objects.get(id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT"):
            return UserWRITESerializer
        else:
            return UserREADSerializer
