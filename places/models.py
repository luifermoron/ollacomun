from django.db import models
import uuid
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4)