"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

app_name ='learning_logs'
urlpatterns = [
    #Página inicial
    path(",views.index,name='index"),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    #path(",include('learning_logs.urls')),
    # Página que mostra todos os tópicos
    path('topics/<int:topic_id>/',views.topics, name='topics'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id/',views.new_entry,name='new_entry')
]
