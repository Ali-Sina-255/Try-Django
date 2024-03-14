from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from . utils import slugify_instance_title
from django.urls import reverse
from django.db.models import Q
from django.conf import settings


User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManger(models.Manager):
    def get_queryset(self):
        # return Articles.objects.filter(lookups)
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Articles(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = ArticleManger()

    def get_absolute_url(self):
        # return f"/article_detail/{self.slug}/"
        return reverse("article_details", kwargs={"slug": self.slug})

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
