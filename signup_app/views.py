from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from signup_app.models import Topic
from signup_app.models import User
from signup_app.models import UserTopic
import datetime


def index(request):
    topic_list = Topic.objects.order_by('name')
    context = {'topic_list': topic_list} #Sets up the context for index.html
    return render(request,'signup_app/index.html',context)

def submit_form(request):
    if request.method == "POST":
        user_email = request.POST.get("email", "")
        topic_id = request.POST.get("topic_selections", "")
        user = User(email=user_email, signup_date=datetime.datetime.now())
        user.save()
        user_topic = UserTopic(user_id=user, topic_id=topic_id, last_update_time=datetime.datetime.now())
        user_topic.save()
    return HttpResponse("Congratulations!")