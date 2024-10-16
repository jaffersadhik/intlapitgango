from rest_framework import serializers
from .models import WebhookAccount, WebhookCustomer, WebhookParameterIndex

class WebhookAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookAccount
        fields = '__all__'


class WebhookCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookCustomer
        fields = '__all__'


class WebhookParameterIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookParameterIndex
        fields = '__all__'
