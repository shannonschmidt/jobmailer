from django.contrib import admin
# Register your models here.
from signup_app.models import User, Topic, UserTopic
class UserTopicsInline(admin.TabularInline): #or StackedInline
    model = UserTopic #The model connected
    extra = 3 #enough space for three extra Topics
class UserAdmin(admin.ModelAdmin):
    fields = ['email','signup_date']
    inlines=[UserTopicsInline] #Connection to Topics
    list_display = ('email','signup_date')
    list_filter = ['signup_date']
    search_field =['email']
admin.site.register(User, UserAdmin)
admin.site.register(Topic)