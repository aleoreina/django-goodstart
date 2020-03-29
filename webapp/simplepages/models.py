from django.db import models
from django.urls import reverse

class Page (models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('page-view', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        