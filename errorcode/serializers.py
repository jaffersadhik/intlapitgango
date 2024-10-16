from rest_framework import serializers
from .models import ErrorcodeAccount, ErrorcodeCarrier, ErrorcodePlatform
import base64
from .models import ErrorcodeCustomer

class ErrorcodeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorcodeAccount
        fields = '__all__'

    def to_representation(self, instance):
        """Customize serialization to encode accountname."""
        representation = super().to_representation(instance)
        if representation.get('accountname'):
            # Encode accountname in Base64
            encoded_accountname = base64.b64encode(representation['accountname'].encode('utf-8')).decode('utf-8')
            representation['accountname'] = encoded_accountname
        return representation
class ErrorcodeCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorcodeCarrier
        fields = '__all__'

class ErrorcodePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorcodePlatform
        fields = '__all__'


class ErrorcodeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorcodeCustomer
        fields = '__all__'  # Include all fields from the ErrorcodeCustomer model


# serializers.py

from rest_framework import serializers
from .models import ErrorcodeSmsServiceProvider

class ErrorcodeSmsServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorcodeSmsServiceProvider
        fields = '__all__'  # Include all fields from the ErrorcodeSmsServiceProvider model
