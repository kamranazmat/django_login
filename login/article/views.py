from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.auth import logout, authenticate, login
from django.template import RequestContext
from django.template import Context
from article.models import Article
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# Create your views here.
def hello(request):
    name = "Kamran"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)
"""    
def home(request):
    t = get_template('main.html')
    html = t.render(Context())
    return HttpResponse(html)
"""    
def articles(request):
    language = 'en-us'
    session_language = 'en-us'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
        
    return render_to_response('articles.html',
                             {'articles' : Article.objects.all(),
                              'language' : language})
 
def language(request, language='en-us'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    return response
    
def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('main.html', c)
    
def auth_view(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/welcome')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/invalid')
    return render_to_response('main.html', context_instance=RequestContext(request))
        
@login_required(login_url='/login/')        
def welcome(request):
    #return render(request, "welcome.html", {'username':request.user.username})
    return render_to_response('welcome.html',
                             {'full_name': request.user.username})
    
def invalid_login(request):
    return render_to_response('invalid_login.html')
 
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
