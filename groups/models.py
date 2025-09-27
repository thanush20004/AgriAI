
from django.db import models
from django.conf import settings

class Group(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_groups')
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='member_groups')
	created_at = models.DateTimeField(auto_now_add=True)
