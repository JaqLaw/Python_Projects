from django.urls import path
from . import views

# the url patterns that define the paths and what view function to do
urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
    path('<int:pk>/balance/', views.balance, name='balance'),
]