from django.db import models
from base_entity.models.base_entity_model import BaseEntity
# Create your models here.
class City(BaseEntity):
    name = models.CharField(max_length=250)

def __str__(self):
    return self.name