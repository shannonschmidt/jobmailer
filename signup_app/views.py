from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from signup_app.models import Topic


def index(request):
    topic_list = Topic.objects.order_by('name')
    context = {'topic_list': topic_list} #Sets up the context for index.html
    return render(request,'signup_app/index.html',context)