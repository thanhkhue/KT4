from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 5000)
    publication_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/media',verbose_name='My Photo')
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title