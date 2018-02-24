# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

keywords = ("true", "+", "да")


class Report(models.Model):
    chat_id = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_send = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)


class Message(models.Model):
    chat_id = models.IntegerField()
    message_id = models.IntegerField(unique=True)
    message_text = models.CharField(max_length=255)
    reply_to_message = models.IntegerField(default=0)
    importance = models.IntegerField(default=0)
    report = models.ForeignKey(to=Report, null=True, blank=True)
    saved = models.BooleanField(default=False)


# @receiver(post_save, sender=Message, dispatch_uid="update_stock_count")
# def setimportance(sender, instance, **kwargs):
#     # if "#важно" in instance.text:
#     #     send instant message to all users of this chat

@receiver(pre_save, sender=Message, dispatch_uid="update_importance")
def setimportance(sender, instance, **kwargs):
    if not instance.saved:
        # try:
        #     report = Report.objects.get(chat_id=instance.chat_id, is_active=True, is_send=False)
        # except Report.DoesNotExist:
        #     report = Report.objects.create(chat_id=instance.chat_id)
        instance.report, report = Report.objects.get_or_create(chat_id=instance.chat_id)
        if "#важно" in instance.message_text:
            instance.importance += 10
        # TODO send instant message to all members of this chat

        if instance.reply_to_message:
            try:
                message = Message.objects.get(message_id=instance.reply_to_message)
                message.importance += 1
                message.saved = True
                if any(key in instance.message_text for key in keywords):
                    message.importance += 1
                message.save()
            except Message.DoesNotExist:
                print "Message not found"
