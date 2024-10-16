from rest_framework import serializers
from .models import IpAccount, IpCustomer, IpShared
import base64

class IpAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAccount
        fields = '__all__'

    # Override to_representation to encode specific fields before sending them
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Base64 encode the accountname if it exists
        if instance.accountname:
            representation['accountname'] = base64.b64encode(instance.accountname.encode()).decode('utf-8')

        return representation

class IpCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpCustomer
        fields = '__all__'

class IpSharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpShared
        fields = '__all__'
