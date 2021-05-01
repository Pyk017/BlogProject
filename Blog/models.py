from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.author} ({self.date})'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



    # DataBase Queries

    # python manage.py shell
    # from Blog.models import Post
    # from django.contrib.auth.models import User

    # User.objects.all() => returns a query set result, which contains the users already present in the database
    # User.objects.first() => gives the first user query
    # User.objects.last() => gives the last user query
    # User.objects.filter(username='Prakhar') => it helps to filter the data based on the parameter passed.
    # user = User.objects.filter(username="Prakhar").first()
    # user.id => gives 1 as id same as (user.pk)
    # user = User.objects.get(id=1) => gives the username of the user having id=1.

    # TO create a Post object
    # post = Post(title='Blog', content="FIrst Post Blog!", author=user)
    # post.save()

    # to get all post posted by a particular user
    # user.post_set.all()

    # To create a post from user
    # user.post_set.create(title='Blogx', content='content of blog')

