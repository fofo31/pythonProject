from django.urls import path
from blog import views

urlpatterns = [
    path('date', views.date_actuelle, name='date'),
    path('article/<int:id>', views.lire, name='lire')
]