from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#  DUMMY DATA
# posts = [
#     {
#         'author': "Prakhar Kumar",
#         'title': "Book1",
#         'content': "First Post",
#         'date': 'April 27, 2021'
#     },
#     {
#         'author': "Yush Kumar",
#         'title': "Book2",
#         'content': "Second Post",
#         'date': 'April 28, 2021'
#     },
#     {
#         'author': "Akansha Yush Kumar",
#         'title': "Book3",
#         'content': "Third Post",
#         'date': 'April 29, 2021'
#     }
# ]


# Create your views here.
def home(request):
    # print(list(Post.objects.all()))
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
