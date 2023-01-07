from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User




class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    partnumber = models.CharField(max_length=250)
    past_price = models.CharField(max_length=250)
    past_dollar = models.CharField(max_length=250)
    
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')

    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    #def __str__(self):
        #return f"{ self.partnumber } and { self.new_price }"

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])