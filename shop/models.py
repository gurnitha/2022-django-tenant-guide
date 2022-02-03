# shop/models.

# Django modules
from django.db import models
<<<<<<< HEAD
from django_tenants.models import TenantMixin, DomainMixin
=======
from django_tenants import TenantMixin, DomainMixin
>>>>>>> 66a7d5070e40b2b5c70ac063e88f0a7531d2f8a7

# Create your models here.


# MODEL: Shop as client
class Shop(TenantMixin):

	name = models.CharField(max_length=100)

	# Default true, schema will be authomatically 
	# created and synced when it is save
	auto_create_schema = True

	def __str__(self):
		return self.name 


# MODEL: Domain
class Domain(DomainMixin):
	pass 