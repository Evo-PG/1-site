from django.urls import path
from . import views

# все сылки по сайту
urlpatterns = [
    path('home/', views.homes_site, name="home"),
    path('post/<int:pk>', views.post_description, name="poster"),
    path('category_sort/<int:pk>', views.category_sort, name="category"),
    path('developer/', views.developer, name="developer")
]