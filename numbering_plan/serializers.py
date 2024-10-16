from rest_framework import serializers
from .models import Country, MncMcc, MncMccPrefix, WorldTimezone

# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

# MncMcc Serializer
class MncMccSerializer(serializers.ModelSerializer):
    class Meta:
        model = MncMcc
        fields = '__all__'

# MncMccPrefix Serializer
class MncMccPrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = MncMccPrefix
        fields = '__all__'

# WorldTimezone Serializer
class WorldTimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldTimezone
        fields = '__all__'
