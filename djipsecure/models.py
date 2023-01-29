from django.db import models
from django.contrib.auth.models import User


class UserIPAddress(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ip_address")
	ip_address = models.GenericIPAddressField()
	is_allowed = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'User IP Address'
		verbose_name_plural = 'User IP Addresses'
