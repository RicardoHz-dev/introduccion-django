from django.urls import path
from .views import BlogListView
app_name = 'blog'


# ACCEDER A TODAS LAS VISTAS QUE CREAREMOS DEL BLOG
urlpatterns = [
    path('', BlogListView.as_view(), name='home')
]

