from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

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
from .serializers import (
    CostCarrierSerializer,
    CostCarrierInvoiceDateSerializer,
    CostCarrierMncmccSerializer,
    CostCarrierMncmccInvoiceDateSerializer,
    CostSMSCSerializer,
    CostSMSCInvoiceDateSerializer,
    CostSMSCmncmccSerializer,
    CostSMSCmncmccInvoiceDateSerializer,
)

# ---- CostCarrier Views ----
class CostCarrierListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            cost_carriers = CostCarrier.objects.filter(
                Q(name__icontains=search_query) |  # Change `name` to the actual field name
                Q(description__icontains=search_query)  # Add more fields as needed
            )
        else:
            cost_carriers = CostCarrier.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(cost_carriers, page_size)
        paginated_cost_carriers = paginator.get_page(page)
        serializer = CostCarrierSerializer(paginated_cost_carriers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_cost_carriers.number,
            'total_items': paginator.count
        })

class CostCarrierCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Set created_date to the current datetime in ISO format
        request.data['created_date'] = datetime.now().isoformat()
        
        serializer = CostCarrierSerializer(data=request.data)

        if serializer.is_valid():
            # Check if a CostCarrier with the same carriername and cost exists
            if CostCarrier.objects.filter(
                carriername=serializer.validated_data['carriername'], 
                dial_in_code=serializer.validated_data['dial_in_code']  # Add this line
            ).exists():
                return Response(
                    {"error": "Combination of carriername, and dial_in_code must be unique."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()  # Save the object if unique
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CostCarrierUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Set the current time for update_date
        cost_id = request.data.get('cost_id')
        cost_carrier = get_object_or_404(CostCarrier, cost_id=cost_id)
        
    

        serializer = CostCarrierSerializer(cost_carrier, data=data, partial=True)
        
        if serializer.is_valid():
            # if CostCarrier.objects.filter(
            #     carriername=serializer.validated_data['carriername'], 
            #     dial_in_code=serializer.validated_data['dial_in_code']  # Add this line
            # ).exists():
            #     return Response(
            #         {"error": "Combination of carriername,  and dial_in_code must be unique."}, 
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ---- CostCarrierInvoiceDate Views ----
class CostCarrierInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            invoice_dates = CostCarrierInvoiceDate.objects.filter(
                Q(invoice_date__icontains=search_query)  # Change to actual fields
            )
        else:
            invoice_dates = CostCarrierInvoiceDate.objects.all()

        paginator = Paginator(invoice_dates, page_size)
        paginated_invoice_dates = paginator.get_page(page)
        serializer = CostCarrierInvoiceDateSerializer(paginated_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_dates.number,
            'total_items': paginator.count
        })

class CostCarrierInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CostCarrierInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostCarrierInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        price_id = request.data.get('price_id')
        invoice_date = get_object_or_404(CostCarrierInvoiceDate, price_id=price_id)
        serializer = CostCarrierInvoiceDateSerializer(invoice_date, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---- CostCarrierMncmcc Views ----
class CostCarrierMncmccListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            mncmccs = CostCarrierMncmcc.objects.filter(
                Q(carriername__icontains=search_query) | Q(cost__icontains=search_query) # Change to actual fields
            )
        else:
            mncmccs = CostCarrierMncmcc.objects.all()

        paginator = Paginator(mncmccs, page_size)
        paginated_mncmccs = paginator.get_page(page)
        serializer = CostCarrierMncmccSerializer(paginated_mncmccs, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_mncmccs.number,
            'total_items': paginator.count
        })

class CostCarrierMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['created_date'] = datetime.now().isoformat()

        serializer = CostCarrierMncmccSerializer(data=request.data)
        if serializer.is_valid():
            if CostCarrierMncmcc.objects.filter(
                mcc=serializer.validated_data['mcc'],
                mnc=serializer.validated_data['mnc'],
                carriername=serializer.validated_data['carriername'],
                dial_in_code=serializer.validated_data['dial_in_code']
            ).exists():
                return Response(
                    {"error": "Combination of  mcc, mnc, carriername, and dial_in_code must be unique."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostCarrierMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Set the current time for update_date
        cost_id = request.data.get('cost_id')
        
        # Fetch the instance to update
        mncmcc = get_object_or_404(CostCarrierMncmcc, cost_id=cost_id)
        
        # Use the modified data with the update_date
        serializer = CostCarrierMncmccSerializer(mncmcc, data=data, partial=True)
        
        if serializer.is_valid():
            # if CostCarrierMncmcc.objects.filter(
            #     mcc=serializer.validated_data['mcc'],
            #     mnc=serializer.validated_data['mnc'],
            #     carriername=serializer.validated_data['carriername'],
            #     dial_in_code=serializer.validated_data['dial_in_code']
            # ).exists():
            #     return Response(
            #         {"error": "Combination of  mcc, mnc, carriername, and dial_in_code must be unique."}, 
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ---- CostCarrierMncmccInvoiceDate Views ----
class CostCarrierMncmccInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            invoice_dates = CostCarrierMncmccInvoiceDate.objects.filter(
                Q(invoice_date__icontains=search_query)  # Change to actual fields
            )
        else:
            invoice_dates = CostCarrierMncmccInvoiceDate.objects.all()

        paginator = Paginator(invoice_dates, page_size)
        paginated_invoice_dates = paginator.get_page(page)
        serializer = CostCarrierMncmccInvoiceDateSerializer(paginated_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_dates.number,
            'total_items': paginator.count
        })

class CostCarrierMncmccInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CostCarrierMncmccInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostCarrierMncmccInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cost_id = request.data.get('cost_id')
        invoice_date = get_object_or_404(CostCarrierMncmccInvoiceDate, cost_id=cost_id)
        serializer = CostCarrierMncmccInvoiceDateSerializer(invoice_date, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---- CostSMSC Views ----
class CostSMSCListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            smscs = CostSMSC.objects.filter(
                Q(cost__icontains=search_query) |  Q( smscid__icontains=search_query)  # A # Change to actual fields
            )
        else:
            smscs = CostSMSC.objects.all()

        paginator = Paginator(smscs, page_size)
        paginated_smscs = paginator.get_page(page)
        serializer = CostSMSCSerializer(paginated_smscs, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_smscs.number,
            'total_items': paginator.count
        })

class CostSMSCCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['created_date'] = datetime.now().isoformat()

        serializer = CostSMSCSerializer(data=request.data)
        if serializer.is_valid():
            if CostSMSC.objects.filter(
                dial_in_code=serializer.validated_data['dial_in_code'],
                smscid=serializer.validated_data['smscid']
            ).exists():
                return Response(
                    {"error": "Combination of dial_in_code, and smscid must be unique."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostSMSCUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Set the current time for update_date
        cost_id = request.data.get('cost_id')
        cost_id = request.data.get('cost_id')
        smsc = get_object_or_404(CostSMSC, cost_id=cost_id)
       
        serializer = CostSMSCSerializer(smsc, data=request.data, partial=True)
        if serializer.is_valid():
            # if CostSMSC.objects.filter(
            #     dial_in_code=serializer.validated_data['dial_in_code'],
            #     smscid=serializer.validated_data['smscid']
            # ).exists():
            #     return Response(
            #         {"error": "Combination of  dial_in_code, and smscid must be unique."}, 
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---- CostSMSCInvoiceDate Views ----
class CostSMSCInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            invoice_dates = CostSMSCInvoiceDate.objects.filter(
                Q(invoice_date__icontains=search_query)  # Change to actual fields
            )
        else:
            invoice_dates = CostSMSCInvoiceDate.objects.all()

        paginator = Paginator(invoice_dates, page_size)
        paginated_invoice_dates = paginator.get_page(page)
        serializer = CostSMSCInvoiceDateSerializer(paginated_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_dates.number,
            'total_items': paginator.count
        })

class CostSMSCInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CostSMSCInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostSMSCInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        price_id = request.data.get('price_id')
        invoice_date = get_object_or_404(CostSMSCInvoiceDate, price_id=price_id)
        serializer = CostSMSCInvoiceDateSerializer(invoice_date, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---- CostSMSCmncmcc Views ----
class CostSMSCmncmccListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            mncmccs = CostSMSCmncmcc.objects.filter(
                Q(name__icontains=search_query)  # Change to actual fields
            )
        else:
            mncmccs = CostSMSCmncmcc.objects.all()

        paginator = Paginator(mncmccs, page_size)
        paginated_mncmccs = paginator.get_page(page)
        serializer = CostSMSCmncmccSerializer(paginated_mncmccs, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_mncmccs.number,
            'total_items': paginator.count
        })

class CostSMSCmncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['created_date'] = datetime.now().isoformat()
        serializer = CostSMSCmncmccSerializer(data=request.data)
        if serializer.is_valid():
            if CostSMSCmncmcc.objects.filter(
                smscid=serializer.validated_data['smscid'],
                dial_in_code=serializer.validated_data['dial_in_code'],
                mnc=serializer.validated_data['mnc'],
                mcc=serializer.validated_data['mcc'],
            ).exists():
                return Response(
                    {"error": "Combination of smscid, dial_in_code, mnc, and mcc   must be unique."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostSMSCmncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Create a mutable copy of the request data
        data = request.data.copy()
        # Set the current time for update_date
        data['update_date'] = datetime.now().isoformat()  
        
        # Get the cost_id from the request data
        cost_id = request.data.get('cost_id')
        # Fetch the existing record
        mncmcc = get_object_or_404(CostSMSCmncmcc, cost_id=cost_id)

        # Use the modified data to update the instance
        serializer = CostSMSCmncmccSerializer(mncmcc, data=data, partial=True)
        
        # Validate and save the instance
        if serializer.is_valid():
            # if CostSMSCmncmcc.objects.filter(
            #     smscid=serializer.validated_data['smscid'],
            #     dial_in_code=serializer.validated_data['dial_in_code'],
            #     mnc=serializer.validated_data['mnc'],
            #     mcc=serializer.validated_data['mcc'],
            # ).exists():
            #     return Response(
            #         {"error": "Combination of smscid, dial_in_code, mnc, and mcc   must be unique."},
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            serializer.save()  # This should now save the update_date correctly
            return Response(serializer.data)  # Return the updated data
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

# ---- CostSMSCmncmccInvoiceDate Views ----
class CostSMSCmncmccInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            invoice_dates = CostSMSCmncmccInvoiceDate.objects.filter(
                Q(invoice_date__icontains=search_query)  # Change to actual fields
            )
        else:
            invoice_dates = CostSMSCmncmccInvoiceDate.objects.all()

        paginator = Paginator(invoice_dates, page_size)
        paginated_invoice_dates = paginator.get_page(page)
        serializer = CostSMSCmncmccInvoiceDateSerializer(paginated_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_dates.number,
            'total_items': paginator.count
        })

class CostSMSCmncmccInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CostSMSCmncmccInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CostSMSCmncmccInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cost_id = request.data.get('cost_id')
        invoice_date = get_object_or_404(CostSMSCmncmccInvoiceDate, cost_id=cost_id)
        serializer = CostSMSCmncmccInvoiceDateSerializer(invoice_date, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
