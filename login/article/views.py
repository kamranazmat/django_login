from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from article.models import Article

# Create your views here.
def hello(request):
    name = "Kamran"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)
    
def home(request):
    t = get_template('main.html')
    html = t.render(Context())
    return HttpResponse(html)
    
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
