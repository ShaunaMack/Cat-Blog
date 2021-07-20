from django.shortcuts import render
import datetime
from operator import itemgetter

blog_posts = {
    "post_one": {
        'content': "I am post 1",
        'created_at': datetime.datetime(2021, 7, 12)
    },
    "post_two": {
        'content': "I am post 2",
        'created_at': datetime.datetime(2021, 7, 15)
    },
    "post_three": {
        'content': "I am post 3",
        'created_at': datetime.datetime(2021, 7, 22)
    },
}

# Create your views here.

def index(request):
    return render(request, "blog/index.html")
    # for post in blog_posts.keys():
    #     blog_posts['post']['created_at']

    # dict(sorted(blog_posts.items(), key = itemgetter(1))[2:])
    # return 
    pass


def all_posts(request):
    # return render(request, 'blog/posts.html', {
    #     'blog_posts': blog_posts
    # })
    pass

def post_detail(request):
    pass
