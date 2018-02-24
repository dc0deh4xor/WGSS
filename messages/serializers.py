from rest_framework import serializers

from messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    reply_to_message = serializers.IntegerField(required=False)

    class Meta:
        model = Message
        fields = ('chat_id', 'message_id', 'message_text', 'reply_to_message')


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message_text', 'importance')
