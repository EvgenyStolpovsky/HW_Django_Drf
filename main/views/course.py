from rest_framework import viewsets, mixins
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.models import Course
from main.paginators import MainPaginator
from main.permissions import IsModerator, IsOwner
from main.seriallizers.course import CourseSerializer


# CRUD для моделей курса - ViewSets


class CourseViewSet(viewsets.mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """Представление курса, которое включает в себя механизм CRUD"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator | IsOwner]
    pagination_class = MainPaginator
