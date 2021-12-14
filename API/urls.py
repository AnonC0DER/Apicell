from django.urls import path
from . import views


urlpatterns = [    
    path('', views.AllMethods),
    path('google-search/', views.GOOGLE),
    path('bing-search/', views.BING),
    path('pypi-search/', views.PYPI),
    path('subscene-search/', views.SUBSCENE),
    
]