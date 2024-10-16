from rest_framework import serializers
from .models import (
    PriceAccount,
    PriceAccountInvoiceDate,
    PriceAccountMncmcc,
    PriceAccountMncmccInvoiceDate,
    PriceCustomer,
    PriceCustomerInvoiceDate,
    PriceCustomerMncmcc,
    PriceCustomerMncmccInvoiceDate,
    PriceShared,
    PriceSharedInvoiceDate,
    PriceSharedMncmcc,
    PriceSharedMncmccInvoiceDate
)

import base64

class PriceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAccount
        fields = '__all__'

    # Override the to_representation method to encode accountname in Base64
    def to_representation(self, instance):
        # Get the original representation of the instance
        representation = super().to_representation(instance)
        
        # Encode the accountname in Base64 if it exists
        accountname = representation.get('accountname', None)
        if accountname:
            encoded_accountname = base64.b64encode(accountname.encode('utf-8')).decode('utf-8')
            representation['accountname'] = encoded_accountname

        return representation

class PriceAccountInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAccountInvoiceDate
        fields = '__all__'


class PriceAccountMncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAccountMncmcc
        fields = '__all__'
        # Override the to_representation method to encode accountname in Base64
    def to_representation(self, instance):
        # Get the original representation of the instance
        representation = super().to_representation(instance)
        
        # Encode the accountname in Base64 if it exists
        accountname = representation.get('accountname', None)
        if accountname:
            encoded_accountname = base64.b64encode(accountname.encode('utf-8')).decode('utf-8')
            representation['accountname'] = encoded_accountname

        return representation


class PriceAccountMncmccInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAccountMncmccInvoiceDate
        fields = '__all__'


class PriceCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCustomer
        fields = '__all__'


class PriceCustomerInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCustomerInvoiceDate
        fields = '__all__'

class PriceCustomerMncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCustomerMncmcc
        fields = '__all__'

class PriceCustomerMncmccInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCustomerMncmccInvoiceDate
        fields = '__all__'

class PriceSharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceShared
        fields = '__all__'

class PriceSharedInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSharedInvoiceDate
        fields = '__all__'

class PriceSharedMncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSharedMncmcc
        fields = '__all__'

class PriceSharedMncmccInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSharedMncmccInvoiceDate
        fields = '__all__'