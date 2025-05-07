from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_dishes, name='category_dishes'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
]
