from django.db import models
import uuid


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):  # __unicode__ on Python 2
        return self.name +  "  Estado = " + "Activo" if self.is_active else "Inactivo"

    def generate_uuid(self):
        self.uuid = uuid.uuid4()
        self.save(update_fields=["uuid"])
