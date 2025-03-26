'''Define padrões URL para contas'''
from django.urls import path,include

app_name = 'accounts'
urlpatterns = [
    #Inclui URLs de autenticação default
    path('',include('django.contrib.auth.urls')),
]