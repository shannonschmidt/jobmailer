from django.contrib import admin
# Register your models here.
from signup_app.models import User, Topic
class UserAdmin(admin.ModelAdmin):
    fields = ['email','signup_date', 'topics']
    list_display = ('email','signup_date', 'get_topics')
    list_filter = ['signup_date']
    search_field =['email']
admin.site.register(User, UserAdmin)
admin.site.register(Topic)