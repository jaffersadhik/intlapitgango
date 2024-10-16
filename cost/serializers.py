from rest_framework import serializers
from .models import (
    CostCarrier,
    CostCarrierInvoiceDate,
    CostCarrierMncmcc,
    CostCarrierMncmccInvoiceDate,
    CostSMSC,
    CostSMSCInvoiceDate,
    CostSMSCmncmcc,
    CostSMSCmncmccInvoiceDate,
)

class CostCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCarrier
        fields = '__all__'

class CostCarrierInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCarrierInvoiceDate
        fields = '__all__'

class CostCarrierMncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCarrierMncmcc
        fields = '__all__'

class CostCarrierMncmccInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCarrierMncmccInvoiceDate
        fields = '__all__'

class CostSMSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostSMSC
        fields = '__all__'

class CostSMSCInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostSMSCInvoiceDate
        fields = '__all__'

class CostSMSCmncmccSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostSMSCmncmcc
        fields = '__all__'

class CostSMSCmncmccInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostSMSCmncmccInvoiceDate
        fields = '__all__'
