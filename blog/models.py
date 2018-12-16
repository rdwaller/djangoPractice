from django.db import models

#Look at models in django docs
class Post(models.Model):
  title = models.CharField(max_length=140)
  body = models.TextField()
  image = models.ImageField(blank=True, null=True ,upload_to='../media/%Y/%m/%d')
  date = models.DateTimeField()

  def __str__(self):
    return self.title