from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet  # make sure you have a ViewSet for Student

# Create a router and register your viewset
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

# Include router URLs
urlpatterns = [
    path('', include(router.urls)),  # all API URLs go through router
]
