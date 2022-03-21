from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=('-created_at',)

class Comments(models.Model):
    post=models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    