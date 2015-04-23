from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from signup_app.model_forms import UserForm
from signup_app.models import Topic
from signup_app.models import User
from signup_app.models import UserTopic
import datetime


def index(request):
    print("entered index method")
    if request.method == "POST":
        print("POST")
        form = UserForm(request.POST or None)
        if (form.is_valid()):
            user_email = request.POST.get("email", "")
            topic_id = request.POST.get("topic_selections", "")
            selected_topic = get_object_or_404(Topic, pk=topic_id)
            user = User(email=user_email, signup_date=datetime.datetime.now())
            user.save()
            user_topic = UserTopic(user_id=user, topic_id=selected_topic, last_update_time=datetime.datetime.now())
            user_topic.save()
            return HttpResponse("Congratulations!")
        else:
            print(form.errors)
            return HttpResponse("Errors")
    else:
        topic_list = Topic.objects.order_by('name')
        context = {'topic_list': topic_list} #Sets up the context for index.html
        return render(request,'signup_app/index.html',context)
