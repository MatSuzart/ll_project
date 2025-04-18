from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Entry
        model = Topic
        fields = ['text']
        labels = {'text': forms.Textarea(attrs={'cols':80})}