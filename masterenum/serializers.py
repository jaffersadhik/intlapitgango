from rest_framework import serializers
from .models import IPCheck, MNCMCCCheck, InvoiceType, Protocol, RouteCheck, RouteType, SenderIdCheck, SmsType, Status, PriceCheck

class IPCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPCheck
        fields = '__all__'

class MNCMCCCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNCMCCCheck
        fields = '__all__'

class InvoiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceType
        fields = '__all__'

class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol
        fields = '__all__'

class RouteCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteCheck
        fields = '__all__'

class RouteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteType
        fields = '__all__'

class SenderIdCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderIdCheck
        fields = '__all__'

class SmsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsType
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class PriceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCheck
        fields = '__all__'


from rest_framework import serializers
from .models import SmsServiceProvider

class SmsServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsServiceProvider
        fields = ['smsserviceprovidername', 'created_date']
