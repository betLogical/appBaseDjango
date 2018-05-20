from .models import Address
from rest_framework import serializers


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('address','race','street','avenue','sidewalk','building','floor','name_residence','number_residence',
                  'suburb','fk_user','fk_city')