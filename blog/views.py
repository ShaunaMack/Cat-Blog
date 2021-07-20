from django.shortcuts import render
from datetime import date
from operator import itemgetter

all_posts = [
    {
        'slug': "richard-good-one",
        'image': "catdesk.JPG",
        'date': date(2021, 7, 12),
        'title': "good one",
        'excerpt': "meow meow meow woof meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow ",
        'content': "meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow eow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow eow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow"

    },
    {
        'slug': "richard-good-two",
        'image': "dundee.JPG",
        'date': date(2021, 7, 13),
        'title': "vg one",
        'excerpt': "lick meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow ",
        'content': """
        meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow eow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow eow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow 
        """

    },
    {
        'slug': "richard-good-three",
        'image': "Rick.JPG",
        'date': date(2021, 7, 21),
        'title': "b one",
        'excerpt': "purrkfsfd meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow ",
        'content': """
        meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow eow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow eow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow 
        """

    }
]

# Create your views here.\

# date helper


def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })
    # for post in blog_posts.keys():
    #     blog_posts['post']['created_at']

    # dict(sorted(blog_posts.items(), key = itemgetter(1))[2:])
    # return
    pass


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })
    # return render(request, 'blog/posts.html', {
    #     'blog_posts': blog_posts
    # })
    pass


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
    pass
