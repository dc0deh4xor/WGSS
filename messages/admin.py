# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from messages.models import Message, Report


class MessageAdmin(admin.ModelAdmin):
    fields = ('message_id', 'chat_id', 'importance', 'report')


admin.site.register(Message, MessageAdmin)
admin.site.register(Report)
