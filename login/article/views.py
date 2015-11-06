from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import get_template
from django.contrib import auth
from django.template import RequestContext
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# Create your views here.
   
def login(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect('/welcome')
    else:
        return render_to_response('login.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)        
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/welcome')
    else:
        return HttpResponseRedirect('/invalid')
    #return render_to_response('main.html', context_instance=RequestContext(request))
        
@login_required(login_url='/login/')        
def welcome(request):
    #return render(request, "welcome.html", {'username':request.user.username})
    return render_to_response('welcome.html',
                             {'full_name': request.user.username})
    
def invalid_login(request):
    return render_to_response('invalid_login.html')
 
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    
def error(request):
    return render_to_response('404.html')
    
