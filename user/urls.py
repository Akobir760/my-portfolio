from django.urls import path

from user.views import my_portfolio


urlpatterns = [
    path('', my_portfolio), 
]
