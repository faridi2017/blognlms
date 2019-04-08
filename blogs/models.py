from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    datemodified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    numberofcomment = models.SmallIntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'Blog'
        verbose_name_plural = "Blog"

class BlogImage(models.Model):
    blogid = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='blog_image')
    image = models.FileField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'BlogImage'
        verbose_name_plural = "BlogImage"

class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    content = models.TextField()
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='blog_comments', null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'Comment'
        verbose_name_plural = "Comment"

class Bloguser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=128)
    confirmemail = models.PositiveSmallIntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'Bloguser'
        verbose_name_plural = "Bloguser"
