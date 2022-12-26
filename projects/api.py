from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() #to see all the data from a table
    permission_classes = [permissions.AllowAny] #permissions, who can make queries
    serializer_class = ProjectSerializers #