from django.urls import path
from .views import  *
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
     path('search/', SearchView.search, name='search')
    
]
