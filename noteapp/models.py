from django.db import models


class Notess(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
