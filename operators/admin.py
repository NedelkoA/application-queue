from django.contrib import admin

from .models import MyApplication, ChangeLog

admin.site.register(MyApplication)
admin.site.register(ChangeLog)
