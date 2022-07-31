from django import forms

class Form_Index(forms.Form):

    name = forms.CharField(label='Запрос для парсинга')
