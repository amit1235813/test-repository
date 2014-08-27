from django.shortcuts import render, render_to_response, RequestContext

from .models import Questions

# Create your views here.

def home(request):

    return render_to_response('homepage.html',
                              locals(),
                              context_instance = RequestContext(request))

def page2_1(request):

    return render_to_response('page2_1.html',
                              locals(),
                              context_instance = RequestContext(request))

def aboutus(request):

    return render_to_response('aboutus.html',
                              locals(),
                              context_instance = RequestContext(request))

def questionlook(request):

    show_questions = Questions.objects.all()

    return render_to_response('questionlook.html', {'Questions': show_questions},
                              context_instance = RequestContext(request))

def a05_02(request):

    return render_to_response('a05_02.html',
                              locals(),
                              context_instance = RequestContext(request))