from django.db import models

# Create your models here.
class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=16)
    content = models.TextField()
    created = models.DateTimeField( auto_now_add=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title