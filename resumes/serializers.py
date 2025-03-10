from rest_framework import serializers
from .models import Resume, Education

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'user', 'title', 'summary', 'skills', 'experience', 'file']  # Include the file field

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'resume', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']