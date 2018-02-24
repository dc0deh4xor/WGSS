# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from messages.models import Message, Report
from messages.serializers import MessageSerializer, ReportSerializer


# Create your views here.


class MessagesCreate(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportList(APIView):
    def get_objects(self, chat_id):

        try:
            return Message.objects.filter(report__chat_id=chat_id, report__is_active=True,
                                          importance__gte=4)
        except Message.DoesNotExist:
            raise Http404

    def get(self, request, chat_id):
        messages = self.get_objects(chat_id)
        serializer = ReportSerializer(messages, many=True)
        return Response(serializer.data)
