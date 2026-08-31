from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "blog_app"
urlpatterns = [
    path("post/post_view/", PostListView.as_view(), name="post_list_view"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail_view"),
    path("post/create_view/", PostCreateView.as_view(), name="post_create_view"),
    path(
        "post/<int:pk>/post_update_view/",
        PostUpdateView.as_view(),
        name="post_update_view",
    ),
    path(
        "post/<int:pk>/post_delete_view/",
        PostDeleteView.as_view(),
        name="post_delete_view",
    ),
]
