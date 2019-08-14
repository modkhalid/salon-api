from rest_framework import serializers
from .models import Saloon,Files
class SaloonSearlizer(serializers.HyperlinkedModelSerializer):
   class Meta():
      model=Saloon
      fields=["name","ad_first","ad_second","city","country","pincode","image","password","email"]



class FileSerializer(serializers.HyperlinkedModelSerializer):
   class Meta():
      model=Files
      fields=["image"]