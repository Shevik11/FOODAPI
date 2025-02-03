from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('<int:item_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
