from rest_framework import serializers
from .models import Payment, Invoice, Outstanding

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Or specify the fields explicitly if needed


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'  # Or specify the fields explicitly if needed


class OutstandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outstanding
        fields = '__all__'  # Or specify the fields explicitly if needed
