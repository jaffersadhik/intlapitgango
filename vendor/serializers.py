from rest_framework import serializers
from .models import Carrier,SMSC

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'

import base64
from rest_framework import serializers

class SMSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSC
        fields = '__all__'

    # Override to_representation to encode specific fields before sending them
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Base64 encode the username and password if they exist
        if instance.username:
            representation['username'] = base64.b64encode(instance.username.encode()).decode('utf-8')
        
        if instance.password:
            representation['password'] = base64.b64encode(instance.password.encode()).decode('utf-8')

        return representation
