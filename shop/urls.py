from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('shops/', shops, name='shops'),
    path('categories/', categories, name='categories'),
]