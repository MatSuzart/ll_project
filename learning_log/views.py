from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm
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

def new_topic(request):
    '''Adiciona um tópico novo'''
    if request.method !='POST':
        #Nenhum dado enviado; cria um formulário em branco
        form = TopicForm()
    else:
        #Dados POST enviados;processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

#Exibe um formulário em bracno ou inválido
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context) 