from django.urls import path
from .views import NewsDetailView, NewsListView

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
]
