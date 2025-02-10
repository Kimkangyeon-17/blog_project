from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("search/<str:q>/", views.PostSearch.as_view()),
    path("delete_comment/<int:pk>/", views.CommentDelete.as_view()),
    path("update_comment/<int:pk>/", views.CommentUpdate.as_view()),
    path("category/<str:slug>/", views.category_page),
    path("delete_post/<int:pk>/", views.PostDelete.as_view(), name="post_delete"),
    path("update_post/<int:pk>/", views.PostUpdate.as_view()),
    path("create_post/", views.PostCreate.as_view()),
    path("<int:pk>/new_comment/", views.CommentCreate.as_view()),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("", views.PostList.as_view()),
]
