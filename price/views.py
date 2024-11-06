from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
import base64
from datetime import datetime
from django.db.models import Q

from .models import (
    PriceAccount,
    PriceAccountInvoiceDate,
    PriceAccountMncmcc,
    PriceAccountMncmccInvoiceDate,
    PriceCustomer,
    PriceCustomerInvoiceDate,
)
from .serializers import (
    PriceAccountSerializer,
    PriceAccountInvoiceDateSerializer,
    PriceAccountMncmccSerializer,
    PriceAccountMncmccInvoiceDateSerializer,
    PriceCustomerSerializer,
    PriceCustomerInvoiceDateSerializer,
)


from .models import (
    PriceCustomerMncmcc,
    PriceCustomerMncmccInvoiceDate,
    PriceShared,
    PriceSharedInvoiceDate,
    PriceSharedMncmcc,
    PriceSharedMncmccInvoiceDate
)
from .serializers import (
    PriceCustomerMncmccSerializer,
    PriceCustomerMncmccInvoiceDateSerializer,
    PriceSharedSerializer,
    PriceSharedInvoiceDateSerializer,
    PriceSharedMncmccSerializer,
    PriceSharedMncmccInvoiceDateSerializer
)
from rest_framework.permissions import IsAuthenticated

# ---- PriceAccount Views ----
class PriceAccountListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            accounts = PriceAccount.objects.filter( Q(accountname__icontains=search_query) |  Q(dial_in_code__icontains=search_query)  )
        else:
            accounts = PriceAccount.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = PriceAccountSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class PriceAccountCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        try:
            # Decode Base64-encoded accountname if present
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                print(decoded_accountname,"1")
                data['accountname'] = decoded_accountname
                print(data,"2")

        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        accountname = data.get('accountname')
        dial_in_code = data.get('dial_in_code')

        if PriceAccount.objects.filter(accountname=accountname, dial_in_code=dial_in_code).exists():
            return Response(
                {"error": "An account with this account name and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        data['created_date'] = datetime.now().isoformat()
        serializer = PriceAccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceAccountUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()  # Create a copy of the request data

        try:
            # Decode Base64-encoded accountname if present
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname

        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the account using the price_id
        price_id = data.get('price_id')
        account = get_object_or_404(PriceAccount, price_id=price_id)

        # Use partial=True for partial updates
        serializer = PriceAccountSerializer(account, data=data, partial=True)
        
        if serializer.is_valid():
            # Save the updated account data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ---- PriceAccountInvoiceDate Views ----
class PriceAccountInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            invoice_dates = PriceAccountInvoiceDate.objects.filter(accountname__icontains=search_query)
        else:
            invoice_dates = PriceAccountInvoiceDate.objects.all()

        paginator = Paginator(invoice_dates, page_size)
        paginated_invoice_dates = paginator.get_page(page)
        serializer = PriceAccountInvoiceDateSerializer(paginated_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_dates.number,
            'total_items': paginator.count
        })

class PriceAccountInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PriceAccountInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceAccountInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        invoice_date = get_object_or_404(PriceAccountInvoiceDate, price_id=price_id)  # Retrieve the invoice date using the price_id
        serializer = PriceAccountInvoiceDateSerializer(invoice_date, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated invoice date data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# ---- PriceAccountMncmcc Views ----
class PriceAccountMncmccListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
      
            mncmccs = PriceAccountMncmcc.objects.filter( Q(accountname__icontains=search_query) |  Q(dial_in_code__icontains=search_query) | Q(price__icontains=search_query)   )
        else:
            mncmccs = PriceAccountMncmcc.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(mncmccs, page_size)
        paginated_mncmccs = paginator.get_page(page)
        serializer = PriceAccountMncmccSerializer(paginated_mncmccs, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_mncmccs.number,
            'total_items': paginator.count
        })

class PriceAccountMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        try:
            # Decode Base64-encoded accountname if present
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                print(decoded_accountname,"1")
                data['accountname'] = decoded_accountname
                print(data,"2")

        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        accountname = data.get('accountname')
        dial_in_code = data.get('dial_in_code')
        mcc = data.get('mcc')
        mnc = data.get('mnc')

        if PriceAccountMncmcc.objects.filter(accountname=accountname, dial_in_code=dial_in_code,mnc=mnc,mcc=mcc).exists():
            return Response(
                {"error": "An account with this account name,Mnc,Mcc and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        data['created_date'] = datetime.now().isoformat()

        serializer = PriceAccountMncmccSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceAccountMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        # Decode Base64-encoded accountname if present
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname

        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        price_id = data.get('price_id')  # Get price_id from request data
        mncmcc = get_object_or_404(PriceAccountMncmcc, price_id=price_id)  # Retrieve the mncmcc using the price_id

        # Extract the accountname, dial_in_code, mcc, and mnc from the request data
        accountname = data.get('accountname')
        dial_in_code = data.get('dial_in_code')
        mcc = data.get('mcc')
        mnc = data.get('mnc')

        # Check if any other record with the same accountname, dial_in_code, mcc, and mnc exists (excluding the current record)
        if PriceAccountMncmcc.objects.filter(
            accountname=accountname, dial_in_code=dial_in_code, mcc=mcc, mnc=mnc
        ).exclude(price_id=price_id).exists():
            return Response(
                {"error": "Another account with this account name, Mnc, Mcc, and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Proceed with the update if no duplicates are found
        serializer = PriceAccountMncmccSerializer(mncmcc, data=data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated mncmcc data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# ---- PriceAccountMncmccInvoiceDate Views ----
class PriceAccountMncmccInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            mncmcc_invoice_dates = PriceAccountMncmccInvoiceDate.objects.filter(accountname__icontains=search_query)
        else:
            mncmcc_invoice_dates = PriceAccountMncmccInvoiceDate.objects.all()

        paginator = Paginator(mncmcc_invoice_dates, page_size)
        paginated_mncmcc_invoice_dates = paginator.get_page(page)
        serializer = PriceAccountMncmccInvoiceDateSerializer(paginated_mncmcc_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_mncmcc_invoice_dates.number,
            'total_items': paginator.count
        })

class PriceAccountMncmccInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PriceAccountMncmccInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceAccountMncmccInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        mncmcc_invoice_date = get_object_or_404(PriceAccountMncmccInvoiceDate, price_id=price_id)  # Retrieve the invoice date using the price_id
        serializer = PriceAccountMncmccInvoiceDateSerializer(mncmcc_invoice_date, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated invoice date data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# ---- PriceCustomer Views ----
class PriceCustomerListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            customers = PriceCustomer.objects.filter( Q(customername__icontains=search_query) |  Q(dial_in_code__icontains=search_query) | Q(price__icontains=search_query)   )
        else:
            customers = PriceCustomer.objects.all()

        paginator = Paginator(customers, page_size)
        paginated_customers = paginator.get_page(page)
        serializer = PriceCustomerSerializer(paginated_customers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_customers.number,
            'total_items': paginator.count
        })

class PriceCustomerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        customername = data.get('customername')
        dial_in_code = data.get('dial_in_code')

        if PriceCustomer.objects.filter(customername=customername, dial_in_code=dial_in_code).exists():
            return Response(
                {"error": "An Price Customer with this customername name and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PriceCustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceCustomerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        customer = get_object_or_404(PriceCustomer, price_id=price_id)  # Retrieve the customer using the price_id
        serializer = PriceCustomerSerializer(customer, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated customer data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# ---- PriceCustomerInvoiceDate Views ----
class PriceCustomerInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            invoice_dates = PriceCustomerInvoiceDate.objects.filter(customername__icontains=search_query)
        else:
            invoice_dates = PriceCustomerInvoiceDate.objects.all()

        paginator = Paginator(invoice_dates, page_size)
        paginated_invoice_dates = paginator.get_page(page)
        serializer = PriceCustomerInvoiceDateSerializer(paginated_invoice_dates, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_dates.number,
            'total_items': paginator.count
        })

class PriceCustomerInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PriceCustomerInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceCustomerInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        invoice_date = get_object_or_404(PriceCustomerInvoiceDate, price_id=price_id)  # Retrieve the invoice date using the price_id
        serializer = PriceCustomerInvoiceDateSerializer(invoice_date, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated invoice date data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status


# views.py


# PriceCustomerMncmcc Views
class PriceCustomerMncmccListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            customers = PriceCustomerMncmcc.objects.filter( Q(customername__icontains=search_query) |  Q(dial_in_code__icontains=search_query) | Q(price__icontains=search_query)   )
        else:
            customers = PriceCustomerMncmcc.objects.all()

        paginator = Paginator(customers, page_size)
        paginated_customers = paginator.get_page(page)
        serializer = PriceCustomerMncmccSerializer(paginated_customers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_customers.number,
            'total_items': paginator.count
        })


class PriceCustomerMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        customername = data.get('customername')
        dial_in_code = data.get('dial_in_code')
        mnc = data.get('mnc')
        mcc = data.get('mcc')

        if PriceCustomerMncmcc.objects.filter(customername=customername, dial_in_code=dial_in_code,mnc=mnc,mcc=mcc).exists():
            return Response(
                {"error": "An Price Customer Mncmcc with this account name ,Mnc,Mcc and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PriceCustomerMncmccSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceCustomerMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):

        price_id = request.data.get('price_id')  # Get price_id from request data
        customer = get_object_or_404(PriceCustomerMncmcc, price_id=price_id)
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Retrieve the customer using the price_id
        serializer = PriceCustomerMncmccSerializer(customer, data=data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated customer data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# PriceCustomerMncmccInvoiceDate Views
class PriceCustomerMncmccInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        invoice_dates = PriceCustomerMncmccInvoiceDate.objects.all()
        serializer = PriceCustomerMncmccInvoiceDateSerializer(invoice_dates, many=True)
        return Response(serializer.data)

class PriceCustomerMncmccInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PriceCustomerMncmccInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceCustomerMncmccInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        invoice_date = get_object_or_404(PriceCustomerMncmccInvoiceDate, price_id=price_id)  # Retrieve the invoice date using the price_id
        serializer = PriceCustomerMncmccInvoiceDateSerializer(invoice_date, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated invoice date data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# PriceShared Views
class PriceSharedListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            prices = PriceShared.objects.filter( Q(dial_in_code__icontains=search_query) | Q(price__icontains=search_query)   )
        else:
            prices = PriceShared.objects.all()

        paginator = Paginator(prices, page_size)
        paginated_prices = paginator.get_page(page)
        serializer = PriceSharedSerializer(paginated_prices, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_prices.number,
            'total_items': paginator.count
        })


class PriceSharedCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        price = data.get('price')
        dial_in_code = data.get('dial_in_code')

        if PriceShared.objects.filter(price=price, dial_in_code=dial_in_code).exists():
            return Response(
                {"error": "An Price Shared with this price name and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PriceSharedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceSharedUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Copy request data and add update_date field
        data = request.data.copy()
        data['update_date'] =  datetime.now().isoformat()
        
        # Extract price_id from the request data
        price_id = data.get('price_id')
        if not price_id:
            return Response({"error": "price_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the PriceShared object using price_id
        shared_price = get_object_or_404(PriceShared, price_id=price_id)

        # Extract price and dial_in_code from the request data
        price = data.get('price')
        dial_in_code = data.get('dial_in_code')

        # Check if the price and dial_in_code combination already exists (excluding the current instance)
        if PriceShared.objects.filter(price=price, dial_in_code=dial_in_code).exclude(price_id=price_id).exists():
            return Response(
                {"error": "A Price Shared with this price and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Perform a partial update using serializer with partial=True
        serializer = PriceSharedSerializer(shared_price, data=data, partial=True)
        if serializer.is_valid():
            # Save the updated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PriceSharedInvoiceDate Views
class PriceSharedInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        invoice_dates = PriceSharedInvoiceDate.objects.all()
        serializer = PriceSharedInvoiceDateSerializer(invoice_dates, many=True)
        return Response(serializer.data)

class PriceSharedInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PriceSharedInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceSharedInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        invoice_date = get_object_or_404(PriceSharedInvoiceDate, price_id=price_id)  # Retrieve the invoice date using the price_id
        serializer = PriceSharedInvoiceDateSerializer(invoice_date, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated invoice date data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status

# PriceSharedMncmcc Views
class PriceSharedMncmccListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        if search_query:
            mncmccs = PriceSharedMncmcc.objects.filter( Q(dial_in_code__icontains=search_query) | Q(price__icontains=search_query)   )
        else:
            mncmccs = PriceSharedMncmcc.objects.all()

        paginator = Paginator(mncmccs, page_size)
        paginated_mncmccs = paginator.get_page(page)
        serializer = PriceSharedMncmccSerializer(paginated_mncmccs, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_mncmccs.number,
            'total_items': paginator.count
        })


class PriceSharedMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        price = data.get('price')
        dial_in_code = data.get('dial_in_code')
        mnc = data.get('mnc')
        mcc = data.get('mcc')

        if PriceSharedMncmcc.objects.filter(price=price, dial_in_code=dial_in_code,mnc=mnc,mcc=mcc).exists():
            return Response(
                {"error": "An Price Shared Mnc Mcc with this price name Mcc, Mnc and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PriceSharedMncmccSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceSharedMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        # Extract price_id from the request
        price_id = request.data.get('price_id')
        if not price_id:
            return Response({"error": "price_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the PriceSharedMncmcc object using price_id
        mncmcc = get_object_or_404(PriceSharedMncmcc, price_id=price_id)

        # Extract fields to check for duplicates
        price = request.data.get('price')
        dial_in_code = request.data.get('dial_in_code')
        mnc = request.data.get('mnc')
        mcc = request.data.get('mcc')

        # Check if another record with the same price, dial_in_code, mnc, and mcc exists, excluding the current record
        if PriceSharedMncmcc.objects.filter(price=price, dial_in_code=dial_in_code, mnc=mnc, mcc=mcc).exclude(price_id=price_id).exists():
            return Response(
                {"error": "A Price Shared Mnc Mcc with this price, MCC, MNC, and dial-in code already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Perform a partial update using the serializer with partial=True
        serializer = PriceSharedMncmccSerializer(mncmcc, data=data, partial=True)
        if serializer.is_valid():
            # Save the updated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PriceSharedMncmccInvoiceDate Views
class PriceSharedMncmccInvoiceDateListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        invoice_dates = PriceSharedMncmccInvoiceDate.objects.all()
        serializer = PriceSharedMncmccInvoiceDateSerializer(invoice_dates, many=True)
        return Response(serializer.data)

class PriceSharedMncmccInvoiceDateCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PriceSharedMncmccInvoiceDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceSharedMncmccInvoiceDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        price_id = request.data.get('price_id')  # Get price_id from request data
        invoice_date = get_object_or_404(PriceSharedMncmccInvoiceDate, price_id=price_id)  # Retrieve the invoice date using the price_id
        serializer = PriceSharedMncmccInvoiceDateSerializer(invoice_date, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated invoice date data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data with 200 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors with 400 status
