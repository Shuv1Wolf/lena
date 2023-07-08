from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import News


class HomePageView(TemplateView):
    template_name = "application/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.latest('id')
        return context


class NewsPageView(ListView):
    model = News
    template_name = 'application/news.html'
    context_object_name = 'news_list'
    paginate_by = 10  # Количество новостей на странице
    ordering = ['-id']  # Сортировка по id публикации


class SpecificNewsView(TemplateView):
    def get(self, request, id):
        data = News.objects.filter(id=id)
        return render(request, 'application/specific_news.html', {'data': data})

