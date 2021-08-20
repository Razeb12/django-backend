from django.shortcuts import render
from .serializers import JobSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Job
from users.models import Candidate
from users.serializers import CandidateSerializer

# Create your views here.
class JobView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobListView(generics.ListAPIView):
    queryset =  Job.objects.all() 
    serializer_class = JobSerializer

class JobDetailView(APIView):
    def get(self,request,id,format=None):
        try:
            job = Job.objects.get(id=id)

        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)
        
        

        return Response(serializer.data,status=status.HTTP_200_OK)

class ListCandidateView(APIView):
    def get(self,request,id,format=None):
        try:
            job = Job.objects.get(id=id)

        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        candidates = job.candidates.all()
        serializer=  CandidateSerializer(candidates,many=True)
        
        

        return Response(serializer.data,status=status.HTTP_200_OK)
