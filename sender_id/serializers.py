from rest_framework import serializers
from .models import SenderIdAccount, SenderIdCustomer, SenderIdShared

# SenderIdAccount Serializer
import base64
from rest_framework import serializers

class SenderIdAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderIdAccount
        fields = '__all__'

    # Override to_representation to encode the accountname before sending it
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Base64 encode the accountname if it exists
        if instance.accountname:
            encoded_accountname = base64.b64encode(instance.accountname.encode()).decode('utf-8')
            representation['accountname'] = encoded_accountname

        return representation
# SenderIdCustomer Serializer
class SenderIdCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderIdCustomer
        fields = '__all__'

# SenderIdShared Serializer
class SenderIdSharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderIdShared
        fields = '__all__'
