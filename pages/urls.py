from django.urls import path

from .views import HomePageView, NewsPageView, SpecificNewsView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path('news', NewsPageView.as_view(), name="news_page"),
    path("news/<int:id>", SpecificNewsView.as_view(), name='specific_news')
]