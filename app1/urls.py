from django.urls import path,include
from .import views
urlpatterns = [
    path('us', views.us),
]
