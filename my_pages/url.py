from django.urls import path

from my_pages.views import about_view, contact_view, home_view

app_name='pagesapp'

urlpatterns = [
    path('', home_view , name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact') 
]