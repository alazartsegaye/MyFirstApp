from rest_framework import serializers
from .models import JobPost, JobApplication

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

    def get_applications(self, obj):
        applications = obj.applications.all()
        return JobApplicationSerializer(applications, many=True).data

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['applicant', 'applied_at']
