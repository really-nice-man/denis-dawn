from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    text = forms.CharField(max_length=150, label="Название темы")
    class Meta:
        model = Topic
        fields = ['text']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}