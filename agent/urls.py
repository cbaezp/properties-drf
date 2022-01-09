from django.urls import path

from . import views

app_name = "agent"

urlpatterns = [
    path("", views.AgentListView.as_view(), name="agent_list"),
    path("<int:pk>/", views.AgentView.as_view(), name="agent"),
]
