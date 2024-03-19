from django.forms import ModelForm, TextInput, DateInput, Textarea
from .models import Articles
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название новости',
                'class': 'form-control'
            }),
            'anons': TextInput(attrs={
                'placeholder': 'Анонс новости',
                'class': 'form-control'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'content': Textarea(attrs={
                'placeholder': 'Текст новости',
                'class': 'form-control'
            }),
        }