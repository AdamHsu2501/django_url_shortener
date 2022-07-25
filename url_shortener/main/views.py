from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm
# Create your views here.

def home(request):
    template = 'main/home.html'
    context = {}
    
    context['form'] = ShortenerForm()
    
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shorten_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shorten_object.short_url
            long_url = shorten_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        
        context['errors'] = used_form.errors
        return render(request, template, context)
    
    return HttpResponse("hello world")

def redirect_url(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404("Sorry this link is broken :(")    
    