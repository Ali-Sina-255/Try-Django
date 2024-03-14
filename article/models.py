from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify

from . utils import slugify_instance_title

class Articles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField( unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





def article_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(instance, sender, created, *args, **kwargs):
    print('Post Save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Articles)
