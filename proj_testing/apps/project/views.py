from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer
from .services.project_service import (
    create_project,
    get_all_projects,
    update_project,
    delete_project
)

from core.permissions import IsAdminUserRole


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get_queryset(self):
        return get_all_projects()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = create_project(request.user, serializer.validated_data)

        return Response(
            ProjectSerializer(project).data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        project = self.get_object()

        serializer = self.get_serializer(project, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        project = update_project(project, serializer.validated_data)

        return Response(ProjectSerializer(project).data)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        delete_project(project)

        return Response(status=status.HTTP_204_NO_CONTENT)