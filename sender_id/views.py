from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import SenderIdAccount, SenderIdCustomer, SenderIdShared
from .serializers import SenderIdAccountSerializer, SenderIdCustomerSerializer, SenderIdSharedSerializer
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
import base64

# ---- SenderIdAccount Views ----

class SenderIdAccountListView(APIView):
    def get(self, request):
        # Fetch query parameters for pagination and search
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        # Filter based on search query if provided
        if search_query:
            accounts = SenderIdAccount.objects.filter(
                Q(accountname__icontains=search_query) |  # Adjust to relevant fields in your model
                Q(senderid__icontains=search_query)
            )
        else:
            accounts = SenderIdAccount.objects.all().order_by('-accountsenderid_id')

        # Implement pagination
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        
        # Serialize the paginated data
        serializer = SenderIdAccountSerializer(paginated_accounts, many=True)

        # Return paginated response
        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class SenderIdAccountCreateView(APIView):
    def post(self, request):
        data = request.data.copy()

        try:
            # Decode Base64-encoded accountname if present
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the combination of senderid and accountname already exists
        senderid = data.get('senderid')
        accountname = data.get('accountname')

        if SenderIdAccount.objects.filter(senderid=senderid, accountname=accountname).exists():
            return Response(
                {"error": "A record with this senderid and accountname combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Set creation and update dates
        data['created_date'] = datetime.now().isoformat()

        serializer = SenderIdAccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SenderIdAccountUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        account_id = data.get('accountsenderid_id')
        
        if not account_id:
            return Response({'detail': 'accountsenderid_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the existing account
        account = get_object_or_404(SenderIdAccount, pk=account_id)

        # Decode Base64-encoded accountname if present
        if 'accountname' in data:
            try:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
            except (base64.binascii.Error, UnicodeDecodeError) as e:
                return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Check if the combination of senderid and accountname already exists
        senderid = data.get('senderid')
        accountname = data.get('accountname')

        if SenderIdAccount.objects.filter(senderid=senderid, accountname=accountname).exists():
            return Response(
                {"error": "A record with this senderid and accountname combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Optional: Set the updated date if necessary
        data['updated_date'] = datetime.now().isoformat()

        # Validate and save the updated data
        serializer = SenderIdAccountSerializer(account, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---- SenderIdCustomer Views ----

class SenderIdCustomerListView(APIView):
    def get(self, request):
        # Fetch query parameters for pagination and search
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        # Filter based on search query if provided
        if search_query:
            customers = SenderIdCustomer.objects.filter(
                Q(customername__icontains=search_query) |  # Adjust to relevant fields in your model
                Q(senderid__icontains=search_query)
            )
        else:
            customers = SenderIdCustomer.objects.all().order_by('-customersenderid_id')

        # Implement pagination
        paginator = Paginator(customers, page_size)
        paginated_customers = paginator.get_page(page)
        
        # Serialize the paginated data
        serializer = SenderIdCustomerSerializer(paginated_customers, many=True)

        # Return paginated response
        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_customers.number,
            'total_items': paginator.count
        })

class SenderIdCustomerCreateView(APIView):
    def post(self, request):
        data = request.data.copy()

        # Set created date
        data['created_date'] = datetime.now().isoformat()

        # Get senderid and customername from the request data
        senderid = data.get('senderid')
        customername = data.get('customername')

        # Check if a record with the same senderid and customername already exists
        if SenderIdCustomer.objects.filter(senderid=senderid, customername=customername).exists():
            return Response(
                {"error": "A record with this senderid and customername combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Proceed to save the data if no duplicate is found
        serializer = SenderIdCustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SenderIdCustomerUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        customer_id = data.get('customersenderid_id')

        if not customer_id:
            return Response({'detail': 'customersenderid_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        customer = get_object_or_404(SenderIdCustomer, pk=customer_id)

        # Get senderid and customername from the request data
        senderid = data.get('senderid')
        customername = data.get('customername')

        if SenderIdCustomer.objects.filter(senderid=senderid, customername=customername).exists():
            return Response(
                {"error": "A record with this senderid and customername combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Add update_date field with the current datetime
        data['update_date'] = datetime.now()

        serializer = SenderIdCustomerSerializer(customer, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---- SenderIdShared Views ----
class SenderIdSharedListView(APIView):
    def get(self, request):
        # Fetch query parameters for pagination and search
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        # Filter based on search query if provided
        if search_query:
            shared_ids = SenderIdShared.objects.filter(
                Q(shared_name__icontains=search_query) |  # Adjust to relevant fields in your model
                Q(senderid__icontains=search_query)
            )
        else:
            shared_ids = SenderIdShared.objects.all().order_by('-senderid_id')

        # Implement pagination
        paginator = Paginator(shared_ids, page_size)
        paginated_shared_ids = paginator.get_page(page)

        # Serialize the paginated data
        serializer = SenderIdSharedSerializer(paginated_shared_ids, many=True)

        # Return paginated response
        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_shared_ids.number,
            'total_items': paginator.count
        })
class SenderIdSharedCreateView(APIView):
    def post(self, request):
        data = request.data.copy()

        # Set created date
        data['created_date'] = datetime.now().isoformat()

        # Get senderid from the request data
        senderid = data.get('senderid')

        # Check if the senderid already exists in the database
        if SenderIdShared.objects.filter(senderid=senderid).exists():
            return Response(
                {"error": "A record with this senderid already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Proceed to save the data if no duplicate is found
        serializer = SenderIdSharedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SenderIdSharedUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        shared_id = data.get('senderid_id')

        if not shared_id:
            return Response({'detail': 'senderid_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the SenderIdShared object
        shared = get_object_or_404(SenderIdShared, pk=shared_id)
        # Get senderid from the request data
        senderid = data.get('senderid')

        # Check if the senderid already exists in the database
        if SenderIdShared.objects.filter(senderid=senderid).exists():
            return Response(
                {"error": "A record with this senderid already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Add the current datetime to the update_date field
        data['update_date'] = datetime.now()

        # Pass the modified data to the serializer
        serializer = SenderIdSharedSerializer(shared, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
