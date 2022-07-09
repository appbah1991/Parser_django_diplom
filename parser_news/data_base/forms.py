from django import forms

class Form_Index(forms.Form):

    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')