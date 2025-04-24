from django.db import models

# Create your models here.
class Dashboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()
    users = models.ManyToManyField('accounts.User', blank=True, related_name='dashboards')

    def __str__(self):
        return self.name