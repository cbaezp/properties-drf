from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Agent
from .serializers import AgentSerializer


class AgentListView(ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None


class AgentView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
