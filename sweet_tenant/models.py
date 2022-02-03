# sweet_tenant/models.py

# Django modules
from django.db import models
from sweet_shared.models import SweetType

# Create your models here.


class Sweet(models.Model):
	sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name 