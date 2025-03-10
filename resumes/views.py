from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Resume, Education
from .serializers import ResumeSerializer, EducationSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        resume_id = self.kwargs['resume_id']
        return Education.objects.filter(resume_id=resume_id)

    def perform_create(self, serializer):
        resume_id = self.kwargs['resume_id']
        resume = Resume.objects.get(id=resume_id)
        serializer.save(resume=resume)