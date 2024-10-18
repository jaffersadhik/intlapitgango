from rest_framework import serializers
from .models import WebhookAccount, WebhookCustomer, WebhookParameterIndex
import base64
class WebhookAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookAccount
        fields = '__all__'
            # Override to_representation to encode specific fields before sending them
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Base64 encode the accountname if it exists
        if instance.accountname:
            representation['accountname'] = base64.b64encode(instance.accountname.encode()).decode('utf-8')

        return representation


class WebhookCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookCustomer
        fields = '__all__'


class WebhookParameterIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookParameterIndex
        fields = '__all__'
