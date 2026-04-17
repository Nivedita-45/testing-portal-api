# from django.shortcuts import render
# from rest_framework import viewsets

# from .serializers import ModuleSerializer, ScreenSerializer

# # Create your views here.
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status

# from core.permissions import IsAdminUserRole
# from rest_framework.permissions import IsAuthenticated



# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# from core.permissions import IsAdminUserRole

# from .models import Project, Module, Screen
# from .serializers import ProjectSerializer, ModuleSerializer, ScreenSerializer   # ✅ FIX
# from .services.project_service import *
# from .services.module_service import ModuleService
# from .services.screen_service import ScreenService

# from .models import Project
# from .serializers import ProjectSerializer
# from .services.project_service import (
#     create_project,
#     get_all_projects,
#     update_project,
#     delete_project
# )

# from core.permissions import IsAdminUserRole


# class ProjectViewSet(ModelViewSet):
#     serializer_class = ProjectSerializer

#     permission_classes = [IsAuthenticated, IsAdminUserRole]

#     def get_queryset(self):
#         return get_all_projects()

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         project = create_project(request.user, serializer.validated_data)

#         return Response(
#             ProjectSerializer(project).data,
#             status=status.HTTP_201_CREATED
#         )

#     def update(self, request, *args, **kwargs):
#         project = self.get_object()

#         serializer = self.get_serializer(project, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)

#         project = update_project(project, serializer.validated_data)

#         return Response(ProjectSerializer(project).data)

#     def destroy(self, request, *args, **kwargs):
#         project = self.get_object()
#         delete_project(project)

#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class ModuleViewSet(viewsets.ModelViewSet):
#     serializer_class = ModuleSerializer
#     permission_classes = [IsAuthenticated, IsAdminUserRole]

#     def get_queryset(self):
#         return ModuleService.get_all_modules()

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         module = ModuleService.create_module(request.user, serializer.validated_data)

#         return Response(ModuleSerializer(module).data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):
#         module = self.get_object()

#         serializer = self.get_serializer(module, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)

#         module = ModuleService.update_module(module, serializer.validated_data)

#         return Response(ModuleSerializer(module).data)

#     def destroy(self, request, *args, **kwargs):
#         module = self.get_object()
#         ModuleService.delete_module(module)

#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class ScreenViewSet(viewsets.ModelViewSet):
#     serializer_class = ScreenSerializer
#     permission_classes = [IsAuthenticated, IsAdminUserRole]

#     def get_queryset(self):
#         return ScreenService.get_all_screens()

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         screen = ScreenService.create_screen(serializer.validated_data)

#         return Response(ScreenSerializer(screen).data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):
#         screen = self.get_object()

#         serializer = self.get_serializer(screen, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)

#         screen = ScreenService.update_screen(screen, serializer.validated_data)

#         return Response(ScreenSerializer(screen).data)

#     def destroy(self, request, *args, **kwargs):
#         screen = self.get_object()
#         ScreenService.delete_screen(screen)

#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAdminUserRole

from .models import Project, Module, Screen
from .serializers import ProjectSerializer, ModuleSerializer, ScreenSerializer
from .services.project_service import (
    create_project,
    get_all_projects,
    update_project,
    delete_project
)
from .services.module_service import ModuleService
from .services.screen_service import ScreenService


# ---------------- PROJECT ----------------
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get_queryset(self):
        return get_all_projects()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = create_project(request.user, serializer.validated_data)

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

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


# ---------------- MODULE ----------------
class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get_queryset(self):
        return ModuleService.get_all_modules()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        module = ModuleService.create_module(request.user, serializer.validated_data)

        return Response(ModuleSerializer(module).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        module = self.get_object()

        serializer = self.get_serializer(module, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        module = ModuleService.update_module(module, serializer.validated_data)

        return Response(ModuleSerializer(module).data)

    def destroy(self, request, *args, **kwargs):
        module = self.get_object()
        ModuleService.delete_module(module)

        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------- SCREEN ----------------
class ScreenViewSet(viewsets.ModelViewSet):
    serializer_class = ScreenSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get_queryset(self):
        return ScreenService.get_all_screens()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        screen = ScreenService.create_screen(serializer.validated_data)

        return Response(ScreenSerializer(screen).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        screen = self.get_object()

        serializer = self.get_serializer(screen, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        screen = ScreenService.update_screen(screen, serializer.validated_data)

        return Response(ScreenSerializer(screen).data)

    def destroy(self, request, *args, **kwargs):
        screen = self.get_object()
        ScreenService.delete_screen(screen)

        return Response(status=status.HTTP_204_NO_CONTENT)