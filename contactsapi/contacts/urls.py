from django.urls import path,include
from .views import *

urlpatterns = [
    path("",ContactList.as_view()),
    path("<int:id>", ContactDetailView.as_view()),
]
