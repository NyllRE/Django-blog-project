from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class blogPost(models.Model):                              # SET_NULL
  user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
  title = models.TextField()
  slug = models.SlugField(unique=True)
  content = models.TextField(null=True, blank=True)
  likes = models.IntegerField()

  def get_absolute_url(self):
    return f"/blog/{self.slug}"

  def get_edit_url(self):
    return f"/blog/{self.slug}/edit"

  def get_delete_url(self):
    return f"/blog/{self.slug}/delete"
    
  def __str__(self):
    return self.slug
