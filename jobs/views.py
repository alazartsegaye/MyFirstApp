from django.shortcuts import render
from rest_framework import viewsets
from .models import JobPost, JobApplication
from .serializers import JobPostSerializer, JobApplicationSerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user) # Automatically sets the 'applicant' field to the user