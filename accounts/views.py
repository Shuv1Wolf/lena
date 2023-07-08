from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

from accounts.models import CustomUser 


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "account/contactuser/user_detail.html"
    context_object_name = "user_object"


class UserListView(ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter(is_staff=False)
    template_name = "account/contactuser/user_list.html"
    context_object_name = "users"