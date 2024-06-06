from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

# API related imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TeamMemberSerializer, AboutUsSerializer
from .models import TeamMember,AboutUs

import logging

logger = logging.getLogger(__name__)
# Create your views here.


# About Us Model API Class View.
class AboutUsView(APIView):
    
    def get_object(self, pk):
        try:
            return AboutUs.objects.get(pk=pk)
        except AboutUs.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            about_data = self.get_object(pk)
            serializer = AboutUsSerializer(about_data)
        else:
            about_data = AboutUs.objects.all()
            serializer = AboutUsSerializer(about_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        about_data = self.get_object(pk)
        serializer = AboutUsSerializer(about_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        about_data = self.get_object(pk)
        serializer = AboutUsSerializer(about_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        about_data = self.get_object(pk)
        about_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 

# Team Member Model API Class View.
class TeamMemberView(APIView):
    
    def get_object(self, pk):
        try:
            return TeamMember.objects.get(pk=pk)
        except TeamMember.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            team_data = self.get_object(pk)
            serializer = TeamMemberSerializer(team_data)
        else:
            team_data = TeamMember.objects.all()
            serializer = TeamMemberSerializer(team_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        team_data = self.get_object(pk)
        serializer = TeamMemberSerializer(team_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        team_data = self.get_object(pk)
        serializer = TeamMemberSerializer(team_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team_data = self.get_object(pk)
        team_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 