from django.shortcuts import render

# Create your views here

def index(request):
    '''A página inicial para o registro de aprendizagem'''
    return render(request,'learning_logs/index.html')