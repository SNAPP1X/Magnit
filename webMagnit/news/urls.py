from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create_news'),
    path('<int:pk>', views.news_detail_view.as_view(), name='news_detail'),
    path('<int:pk>/update', views.news_update_view.as_view(), name='news_update'),
    path('<int:pk>/delete', views.news_delete_view.as_view(), name='news_delete')
]