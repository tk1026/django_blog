
from django import template
from ..models import Blog, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def archives():
    return Blog.objects.dates('created', 'month', order='DESC')

@register.simple_tag
def categories():
    return Category.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)
    #return Category.objects.all()

@register.simple_tag
def tags():
    return Tag.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)