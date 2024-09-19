# jobs/admin.py
from django.contrib import admin
from .models import Job, Company, UserProfile

admin.site.register(Job)
admin.site.register(Company)
admin.site.register(UserProfile)
