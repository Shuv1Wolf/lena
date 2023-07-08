from django.urls import path, include

from .views import UserListView, UserDetailView


urlpatterns = [
    path("", include("allauth.urls")),
    path("list/", UserListView.as_view(), name="user_list"),
    path("list/<int:pk>", UserDetailView.as_view(), name="user_detail"),
]