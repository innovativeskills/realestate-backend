from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

# API related imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MembershipSerializer
from .models import Membership

import logging

logger = logging.getLogger(__name__)
# Create your views here.


# Membership Model API Class View.
class MembershipView(APIView):
    
    def get_object(self, pk):
        try:
            return Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            membership_data = self.get_object(pk)
            serializer = MembershipSerializer(membership_data)
        else:
            membership_data = Membership.objects.all()
            serializer = MembershipSerializer(membership_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        membership_data = self.get_object(pk)
        serializer = MembershipSerializer(membership_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        membership_data = self.get_object(pk)
        membership_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 