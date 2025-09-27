from django.db import models
from users.models import User

class Connection(models.Model):
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_connections')
	to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_connections')
	status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted')])
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('from_user', 'to_user')
