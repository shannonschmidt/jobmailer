from webscraperapp.models import Job

__author__ = 'shannon'
from django.contrib import admin
# Register your models here.
from signup_app.models import User, Topic
class JobAdmin(admin.ModelAdmin):
    fields = ['posting_date','found_date', 'company', 'title', 'location', 'source', 'link', 'topics']
    list_display = ('posting_date','found_date', 'company', 'title', 'location', 'source', 'link', 'get_topics')
    list_filter = ['found_date']
    search_field =['company']
admin.site.register(Job, JobAdmin)