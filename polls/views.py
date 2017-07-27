from django.http import HttpResponse, Http404
#from django.template import loader
from django.shortcuts import render
from .models import Question

"""
Following index method was used before we applied shortcut.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    # next line was used before applying template
    ##output = ', '.join([q.question_text for q in latest_question_list])
    
    return HttpResponse(template.render(context, request))
"""

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    context = {
        'latest_question_list': latest_question_list
    } 
    
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpsResponse("You're voting on question %s" % question_id)