from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import Payment, Invoice, Outstanding
from .serializers import PaymentSerializer, InvoiceSerializer, OutstandingSerializer

# Payment Views
class PaymentListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            payments = Payment.objects.filter(customername__icontains=search_query)
        else:
            payments = Payment.objects.all().order_by('-payment_date')

        paginator = Paginator(payments, page_size)
        paginated_payments = paginator.get_page(page)
        serializer = PaymentSerializer(paginated_payments, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_payments.number,
            'total_items': paginator.count
        })

class PaymentCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        serializer = PaymentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        payment_id = data.get('payment_id')

        if not payment_id:
            return Response({'detail': 'payment_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        payment = Payment.objects.filter(pk=payment_id).first()

        if not payment:
            return Response({'detail': 'Payment not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(payment, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Invoice Views
class InvoiceListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        invoices = Invoice.objects.all().order_by('-created_date')
        paginator = Paginator(invoices, page_size)
        paginated_invoices = paginator.get_page(page)
        serializer = InvoiceSerializer(paginated_invoices, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoices.number,
            'total_items': paginator.count
        })

class InvoiceCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        serializer = InvoiceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        invoice_id = data.get('invoice_id')

        if not invoice_id:
            return Response({'detail': 'invoice_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        invoice = Invoice.objects.filter(pk=invoice_id).first()

        if not invoice:
            return Response({'detail': 'Invoice not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Outstanding Views
class OutstandingListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        outstandings = Outstanding.objects.all().order_by('-created_date')
        paginator = Paginator(outstandings, page_size)
        paginated_outstandings = paginator.get_page(page)
        serializer = OutstandingSerializer(paginated_outstandings, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_outstandings.number,
            'total_items': paginator.count
        })

class OutstandingCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        serializer = OutstandingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OutstandingUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        outstanding_id = data.get('outstanding_id')

        if not outstanding_id:
            return Response({'detail': 'outstanding_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        outstanding = Outstanding.objects.filter(pk=outstanding_id).first()

        if not outstanding:
            return Response({'detail': 'Outstanding not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OutstandingSerializer(outstanding, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
