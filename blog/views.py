from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


# Complete CRUD
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.all()

        search_query = self.request.GET.get("search", "")

        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(
                catagory__icontains=search_query
            )
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create_form.html"
    fields = ["title", "content", "image", "catagory"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_create_form.html"
    fields = ["title", "content", "image", "catagory"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confrim_delet.html"
    success_url = reverse_lazy("blog_app:post_list_view")
