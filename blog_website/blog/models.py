from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password

class UserTable (models.Model):
    username = models.CharField(max_length=255, unique=True)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.pk or 'password' in self.__dict__:
            self.password = make_password(self.password)
        super(UserTable, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class PostCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PostTable(models.Model):
    post_title = models.CharField(max_length=255, unique=True)
    post_content = models.TextField()
    post_category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    post_publish_date = models.DateField()

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(PostTable, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Comment by {self.user.username} on '{self.post.post_title}'"