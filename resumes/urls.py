from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet, EducationListCreateView

router = DefaultRouter()
router.register(r'resumes', ResumeViewSet, basename='resume')

urlpatterns = [
    path('', include(router.urls)),
    path('resume/<int:resume_id>/educations/', EducationListCreateView.as_view(), name='resume-educations'),
]