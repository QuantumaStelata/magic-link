from django.db import models

# Create your models here.

class Link(models.Model):
    email = models.EmailField('Email')
    token = models.TextField('Token', primary_key=True, max_length=4)
    number_visits = models.TextField('Number of visits', default=0)
    active = models.BooleanField('Activate', default=True)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'