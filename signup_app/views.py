from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from signup_app.model_forms import UserForm
import datetime


def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_obj = form.save(commit=False)#don't commit yet since we need to set the signup date
            user_obj.signup_date = datetime.datetime.now()
            user_obj.save()
            form.save_m2m()

            return render_to_response('signup_app/congrats.html', context_instance=RequestContext(request))
        else:
            print(form.errors)
            return render_to_response('signup_app/error.html', context_instance=RequestContext(request))
    else:
        form = UserForm()
        return render_to_response('signup_app/index.html', {'form':form },
                                 context_instance=RequestContext(request))
        # return HttpResponse("test")
