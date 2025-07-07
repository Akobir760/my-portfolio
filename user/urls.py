from django.urls import path

from user.views import my_portfolio

app_name='users'

urlpatterns = [
    path('portfolio/', my_portfolio), 
]
