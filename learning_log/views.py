from django.shortcuts import render
from .models import Topic
# Create your views here

def index(request):
    '''A página inicial para o registro de aprendizagem'''
    return render(request,'learning_logs/index.html')

def topics(request,topic_id):
    '''Mostra todos os tópicos'''
    topic = Topic.objects.get(id=topic_id)
    entires = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entires':entires}
    return render(request, 'learning_logs/topics.html',context)