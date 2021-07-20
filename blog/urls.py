from django.urls import path
from . import views

urlpatterns = [
    # home with selected posts
    path("", views.index, name="starting-page"),
    # all blog posts
    path("posts", views.all_posts, name="posts-page"),
    # individual blog post page
    # slug is unique-identifier that is SEO and user friendly
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]
