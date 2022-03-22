from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=128, unique=True)
    startDate = models.DateField()
    description = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Courses, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

