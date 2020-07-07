from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='home'),
    path('articles/<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),

    # https://www.tutorialspoint.com/django/django_url_mapping.htm
    path('<field>/', views.articles_for_field, name='articles_for_field'),

]