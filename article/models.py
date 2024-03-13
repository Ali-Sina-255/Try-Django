from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save


class Articles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_pre_save(instance,sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug=slugify(instance.title)

pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(instance,sender,created, *args, **kwargs):
    print('Post Save')
    if created:
        instance.slug=slugify(instance.title)
        instance.save()
        
post_save.connect(article_post_save, sender=Articles)