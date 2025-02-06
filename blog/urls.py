from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
]