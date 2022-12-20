from rest_framework import viewsets
from .filters import (
    StudyFilter,
)
from .models import (
    User,
    Study,
)
from .serializers import (
    UserSerializer,
    StudySerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    filterset_class = StudyFilter
