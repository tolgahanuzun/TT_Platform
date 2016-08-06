from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile


class NewProfile(admin.ModelAdmin):
    inlines = [ProfileInline]
 
admin.site.register(User, NewProfile)