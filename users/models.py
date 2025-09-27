from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	location = models.CharField(max_length=255, blank=True)
	farm_size = models.CharField(max_length=100, blank=True)
	crops_grown = models.TextField(blank=True)  # Comma-separated or use ManyToMany to Crop model
	experience = models.PositiveIntegerField(help_text="Years of experience", default=0)
	profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

	def __str__(self):
		return self.username
