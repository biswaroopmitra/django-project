from django.db import models
from base_entity.models.base_entity_model import BaseEntity
from city.models.city_model import City
# Create your models here.
class University(BaseEntity):
    name =  models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='universities')

