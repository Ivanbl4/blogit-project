from sre_constants import CATEGORY
from django.db import models
from profiles.models import Profile
from comments.models import Comment
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
import uuid


# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICE = (
        'Technology',
        'Lifestyle',
        'Fashion',
        'Art',
        'Food',
        'Architecture',
        'Adventure',
        'Other'
    )
    CATEGORY_CHOICE = tuple(zip(CATEGORY_CHOICE, CATEGORY_CHOICE))
    title = models.CharField(max_length=150)
    text = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=15, default=CATEGORY_CHOICE[-1][0])
    text_slug = models.CharField(max_length=200, default='', blank=True)
    slug = models.CharField(max_length=160, default='', blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d', verbose_name='Blog Image', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comment, blank=True)
    likes = ArrayField(models.IntegerField(), blank=True, default=list, help_text='Collects profile ids as Integer')
    # tags = TaggableManager(blank=True)
    is_published = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return '{0} {1} ({2})'.format(
            self.title[:20] + '...',
            self.author.user.username,
            self.id
        )

    def shorten_text(self):
        self.text_slug = self.text[:197] + '...'

    def get_slug(self):
        return slugify(self.title, allow_unicode=False) + '-{}'.format(str(uuid.uuid1())[:8])

    def check_slug(self):
        # для нового блога
        if not self.slug:
            self.slug = self.get_slug()
        # проверка слага для существующего блога
        else:
            if slugify(self.title, allow_unicode=False) != self.slug[:-9]:
                self.slug = self.get_slug()

    def save(self, *args, **kwargd):
        print('Blog is saving #{}'.format(self.id))
        self.shorten_text()
        self.check_slug()
        super(Blog, self).save(*args, **kwargd)
    

    
    
    
    
    
    