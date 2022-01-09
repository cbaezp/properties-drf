from django.urls import path

from . import views

app_name = "property"

urlpatterns = [
    path("", views.PropertyListView.as_view(), name="property_home"),
    path("<slug:slug>/", views.PropertyView.as_view(), name="property"),
]
