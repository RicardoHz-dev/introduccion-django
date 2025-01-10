from django.urls import path
from .views import BlogListView, BlogCreateView
app_name = 'blog'


# ACCEDER A TODAS LAS VISTAS QUE CREAREMOS DEL BLOG
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create')
]

