from django.urls import path
from .views import legacy_view

urlpatterns = [
    path('legacy/', legacy_view, name='legacy_view'),
]
