from django.db import models

class Topic(models.Model):
    '''Um tópico que o usuário está aprendendo'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Retorna uma representação de string do modelo'''
        return self.text