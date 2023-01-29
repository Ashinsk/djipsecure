from ipware import get_client_ip
from django.contrib import auth
from django.utils.translation import gettext as _
from django.utils.deprecation import MiddlewareMixin

from djipsecure.models import UserIPAddress


class IPSecureMiddleware(MiddlewareMixin):

	def process_request(self, request):
		client_ip, is_routable = get_client_ip(request)
		print("IPMiddleware",client_ip, request.user)

		if request.user.is_superuser:
			pass
		if request.user.is_anonymous:
			pass
		elif request.user.is_authenticated:
			if not UserIPAddress.objects.filter(user=request.user,ip_address=client_ip,is_allowed=True).exists():
				auth.logout(request)
				raise Exception(_(f"You are not allowed to request with IP address {client_ip}"))
		else:
			auth.logout(request)
			raise Exception(_(f"IPSecure has been enabled. Please add your IP address to allow further."))
