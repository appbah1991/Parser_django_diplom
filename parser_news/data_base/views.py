from django.shortcuts import render
from data_base.models import News
from data_base.forms import Form_Index
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def main_view(request):
    if request.method == 'POST':
        form = Form_Index(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                name,
                message,
                'appbah2020@yendex.ru',
                [email],
                fail_silently=True,
            )
        else:
            return render(request, 'data_base/index.html', context={'form': form})
    else:
        form = Form_Index
    return render(request, 'data_base/index.html', context= {'form': form})


class NewsListView(ListView):
    model = News
    template_name = 'data_base/result_bv.html'

class NewsDeleteView(DeleteView):
    template_name = 'data_base/news_delete_confirm.html'
    model = News
    success_url = reverse_lazy('data_base:result_bv')



