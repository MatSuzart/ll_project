from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here

def index(request):
    '''A página inicial para o registro de aprendizagem'''
    return render(request,'learning_logs/index.html')
@login_required
def topics(request,topic_id):
    
    '''Mostra todos os tópicos'''
    topic = Topic.objects.get(id=topic_id)
    # Verifica se o tópico pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404
    
    entires = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entires':entires}
    return render(request, 'learning_logs/topics.html',context)
@login_required
def new_entry(request,topic_id):
    '''Adiciona uma entrada nova para um tópico específico'''
    topic = Topic.objects.get(id=topics)

    if topic.owner !=request.user:
        raise Http404
    if request.method !='POST':
        # Nenhum dado enviado; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados Post enviados;processa os dados
        form = EntryForm(data=request.POST)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return redirect('learning_logs:topic',topic_id=topic_id)
    
    #Exibe um formulário em branco inválido
    context = {'topic':topic,'form':form}
    return render(request, 'learning_logs/new_entry.html',context)
@login_required
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
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context) 