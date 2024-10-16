from rest_framework import serializers
from .models import Account, Company, Customer
# Customer Serializer
import base64
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    # Override to_representation to encode specific fields before sending them
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Base64 encode the loginpassword, username, and password if they exist
        if instance.loginpassword:
            representation['loginpassword'] = base64.b64encode(instance.loginpassword.encode()).decode('utf-8')
        
        if instance.username:
            representation['username'] = base64.b64encode(instance.username.encode()).decode('utf-8')
        
        if instance.password:
            representation['password'] = base64.b64encode(instance.password.encode()).decode('utf-8')

        return representation

# Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    # Override to_representation to encode username and password before sending
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Base64 encode the username if it exists
        if instance.username:
            encoded_username = base64.b64encode(instance.username.encode()).decode('utf-8')
            representation['username'] = encoded_username

        # Base64 encode the password if it exists
        if instance.password:
            encoded_password = base64.b64encode(instance.password.encode()).decode('utf-8')
            representation['password'] = encoded_password

        return representation



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    # Override to_representation to encode the loginpassword before sending it
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Base64 encode the loginpassword if it exists
        if instance.loginpassword:
            encoded_password = base64.b64encode(instance.loginpassword.encode()).decode('utf-8')
            representation['loginpassword'] = encoded_password

        return representation
