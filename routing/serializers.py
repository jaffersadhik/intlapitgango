# serializers.py
from rest_framework import serializers
from .models import Route, RouteAccount, RouteAccountMncmcc, RouteCustomer, RouteCustomerMncMcc,RouteShared, RouteSharedMncmcc
import base64



class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class RouteAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteAccount
        fields = '__all__'  # Include all fields from the RouteAccount model

    # Override to_representation to encode specific fields before sending them
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Base64 encode the accountname if it exists
        if instance.accountname:
            representation['accountname'] = base64.b64encode(instance.accountname.encode()).decode('utf-8')

        return representation

class RouteAccountMncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteAccountMncmcc
        fields = '__all__'
        # Override to_representation to encode specific fields before sending them
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Base64 encode the accountname if it exists
        if instance.accountname:
            representation['accountname'] = base64.b64encode(instance.accountname.encode()).decode('utf-8')

        return representation
class RouteCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteCustomer
        fields = '__all__'

class RouteCustomerMncMccSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteCustomerMncMcc
        fields = '__all__'


class RouteSharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteShared
        fields = '__all__'

class RouteSharedMncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteSharedMncmcc
        fields = '__all__'
