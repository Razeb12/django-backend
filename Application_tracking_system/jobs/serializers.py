from rest_framework import serializers
from .models import Job
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['recruiter','title','company','location','description','skills_req','job_type','link','date_posted']
        

