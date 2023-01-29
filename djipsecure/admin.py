from django.contrib import admin
from djipsecure.models import UserIPAddress


@admin.register(UserIPAddress)
class UserIPAddressAdmin(admin.ModelAdmin):
	list_display = ('user', 'ip_address', 'is_allowed')
	list_filter = ('is_allowed',)
	search_fields = ('user',)

