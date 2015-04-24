from django.shortcuts import render, get_object_or_404, render_to_response
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from signup_app.model_forms import UserForm
from signup_app.models import Topic
from signup_app.models import User
import datetime


def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if (form.is_valid()):
            user_obj = form.save(commit=False)
            user_obj.signup_date = datetime.datetime.now()
            user_obj.save()
            form.save_m2m()
            # user_topic = UserTopic(user_id=user, topic_id=selected_topic, last_update_time=datetime.datetime.now())
            # user_topic.save()
            return HttpResponse("Congratulations!")
        else:
            print(form.errors)
            return HttpResponse("Errors")
    else:
        form = UserForm()
    # return render(request,'signup_app/index.html')
        return render_to_response('signup_app/index.html', {'form':form },
            context_instance=RequestContext(request))
