from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from data_base.models import News, Url, Title
from data_base.forms import Form_Index
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .func import parsing_news
from .serializer import UrlSerializer, TitleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser



def main_view(request):
    if request.method == 'POST':
        form = Form_Index(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            parsing_news(name)
        else:
            return render(request, 'data_base/index.html', context={'form': form})
    else:
        form = Form_Index
    return render(request, 'data_base/index.html', context= {'form': form})


class NewsListView(UserPassesTestMixin, ListView):
    model = News
    template_name = 'data_base/result_bv.html'
    paginate_by = 10
    queryset = News.objects.select_related('title', 'url')


    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('users:login')

class NewsDeleteView(DeleteView):
    template_name = 'data_base/news_delete_confirm.html'
    model = News
    success_url = reverse_lazy('data_base:result_bv')

class UrlViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer





