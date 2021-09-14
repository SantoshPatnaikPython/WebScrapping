from django.urls import path
from .views import details_seek

urlpatterns = [
    path('', details_seek),
]