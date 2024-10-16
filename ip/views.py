from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import IpAccount, IpCustomer, IpShared
from .serializers import IpAccountSerializer, IpCustomerSerializer, IpSharedSerializer
import base64
from datetime import datetime

# IP Account Views

class IpAccountListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            accounts = IpAccount.objects.filter(accountname__icontains=search_query)
        else:
            accounts = IpAccount.objects.all().order_by('-update_date', '-created_date')
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = IpAccountSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class IpAccountCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError):
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)
        
        ip = data.get('ip')
        accountname = data.get('accountname')

        # Check if the combination of ip and accountname already exists
        if IpAccount.objects.filter(ip=ip, accountname=accountname).exists():
            return Response(
                {"error": "A record with this IP and accountname combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        data['created_date'] = datetime.now().isoformat()
        serializer = IpAccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IpAccountUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        account_id = data.get('ipaccount_id')

        if not account_id:
            return Response({'detail': 'ipaccount_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        account = get_object_or_404(IpAccount, pk=account_id)

        if 'accountname' in data:
            try:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
            except (base64.binascii.Error, UnicodeDecodeError):
                return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)
        ip = data.get('ip')
        accountname = data.get('accountname')

        # Check if the combination of ip and accountname already exists
        if IpAccount.objects.filter(ip=ip, accountname=accountname).exists():
            return Response(
                {"error": "A record with this IP and accountname combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        data['update_date'] = datetime.now().isoformat()
        serializer = IpAccountSerializer(account, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# IP Customer Views

class IpCustomerListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            customers = IpCustomer.objects.filter(customername__icontains=search_query)
        else:
            customers = IpCustomer.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(customers, page_size)
        paginated_customers = paginator.get_page(page)
        serializer = IpCustomerSerializer(paginated_customers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_customers.number,
            'total_items': paginator.count
        })

class IpCustomerCreateView(APIView):
    def post(self, request):
        data = request.data.copy()

        # Set created date
        data['created_date'] = datetime.now().isoformat()

        # Extract ip and customername from the request data
        ip = data.get('ip')
        customername = data.get('customername')

        # Check if the combination of ip and customername already exists
        if IpCustomer.objects.filter(ip=ip, customername=customername).exists():
            return Response(
                {"error": "A record with this IP and customername combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Proceed to save the data if no duplicate is found
        serializer = IpCustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IpCustomerUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        customer_id = data.get('ipcustomer_id')

        if not customer_id:
            return Response({'detail': 'ipcustomer_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
 # Extract ip and customername from the request data
        ip = data.get('ip')
        customername = data.get('customername')

        # Check if the combination of ip and customername already exists
        if IpCustomer.objects.filter(ip=ip, customername=customername).exists():
            return Response(
                {"error": "A record with this IP and customername combination already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        customer = get_object_or_404(IpCustomer, pk=customer_id)

       

        data['update_date'] = datetime.now().isoformat()
        serializer = IpCustomerSerializer(customer, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# IP Shared Views

class IpSharedListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            ips = IpShared.objects.filter(ip__icontains=search_query)
        else:
            ips = IpShared.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(ips, page_size)
        paginated_ips = paginator.get_page(page)
        serializer = IpSharedSerializer(paginated_ips, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_ips.number,
            'total_items': paginator.count
        })

class IpSharedCreateView(APIView):
    def post(self, request):
        data = request.data.copy()

        # Extract the IP address from the request data
        ip = data.get('ip')

        # Check if the IP already exists in the IpShared table
        if IpShared.objects.filter(ip=ip).exists():
            return Response(
                {"error": "A record with this IP address already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Set created date
        data['created_date'] = datetime.now().isoformat()

        # Proceed to save the data if the IP is unique
        serializer = IpSharedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IpSharedUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        ip_id = data.get('ip_id')

        if not ip_id:
            return Response({'detail': 'ip_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
# Extract the IP address from the request data
        ip = data.get('ip')

        # Check if the IP already exists in the IpShared table
        if IpShared.objects.filter(ip=ip).exists():
            return Response(
                {"error": "A record with this IP address already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        ip = get_object_or_404(IpShared, pk=ip_id)

        data['update_date'] = datetime.now().isoformat()
        serializer = IpSharedSerializer(ip, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
