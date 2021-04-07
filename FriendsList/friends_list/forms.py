from .models import MyDB
from django.forms import ModelForm, TextInput


class MyDBForm(ModelForm):
    class Meta:
        model = MyDB
        fields = ['name', 'age']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть ім'я"
            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть вік"
            }),
        }


