from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobPostViewSet, basename='job-post')
router.register(r'applications', JobApplicationViewSet, basename='job-application')

urlpatterns = [
    path('', include(router.urls)),
]