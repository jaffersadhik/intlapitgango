from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import WebhookAccount
from .serializers import WebhookAccountSerializer
import base64
import datetime
from rest_framework.permissions import IsAuthenticated

class WebhookAccountListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            accounts = WebhookAccount.objects.filter(accountname__icontains=search_query)
        else:
            accounts = WebhookAccount.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = WebhookAccountSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class WebhookAccountCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError):
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        accountname = data.get('accountname')
        weghookurl = data.get('weghookurl')

        if WebhookAccount.objects.filter(accountname=accountname, weghookurl=weghookurl).exists():
            return Response({"error": "A record with this accountname and webhook URL already exists."}, status=status.HTTP_400_BAD_REQUEST)

        data['created_date'] = datetime.datetime.now().isoformat()
        serializer = WebhookAccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WebhookAccountUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        account_id = data.get('webhookaccount_id')

        if not account_id:
            return Response({'detail': 'webhookaccount_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the current account object
        account = get_object_or_404(WebhookAccount, pk=account_id)

        # Decode 'accountname' if present in the data
        if 'accountname' in data:
            try:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
            except (base64.binascii.Error, UnicodeDecodeError):
                return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        accountname = data.get('accountname')
        weghookurl = data.get('weghookurl')

        # Exclude the current account from the uniqueness check
        if WebhookAccount.objects.filter(accountname=accountname, weghookurl=weghookurl).exclude(pk=account_id).exists():
            return Response({"error": "A record with this accountname and webhook URL already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the account object with the new data
        data['update_date'] = datetime.datetime.now().isoformat()
        serializer = WebhookAccountSerializer(account, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import WebhookCustomer
from .serializers import WebhookCustomerSerializer
import base64
import datetime

class WebhookCustomerListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            customers = WebhookCustomer.objects.filter(customername__icontains=search_query)
        else:
            customers = WebhookCustomer.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(customers, page_size)
        paginated_customers = paginator.get_page(page)
        serializer = WebhookCustomerSerializer(paginated_customers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_customers.number,
            'total_items': paginator.count
        })

class WebhookCustomerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
       

        customername = data.get('customername')
        weghookurl = data.get('weghookurl')

        if WebhookCustomer.objects.filter(customername=customername, weghookurl=weghookurl).exists():
            return Response({"error": "A record with this customername and webhook URL already exists."}, status=status.HTTP_400_BAD_REQUEST)

        data['created_date'] = datetime.datetime.now().isoformat()
        serializer = WebhookCustomerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WebhookCustomerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        customer_id = data.get('webhookcustomer_id')

        if not customer_id:
            return Response({'detail': 'webhookcustomer_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the current customer object
        customer = get_object_or_404(WebhookCustomer, pk=customer_id)

        customername = data.get('customername')
        weghookurl = data.get('weghookurl')

        # Exclude the current customer from the uniqueness check
        if WebhookCustomer.objects.filter(customername=customername, weghookurl=weghookurl).exclude(pk=customer_id).exists():
            return Response({"error": "A record with this customername and webhook URL already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the customer object with the new data
        data['update_date'] = datetime.datetime.now().isoformat()
        serializer = WebhookCustomerSerializer(customer, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import WebhookParameterIndex
from .serializers import WebhookParameterIndexSerializer
import datetime

class WebhookParameterIndexListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            parameters = WebhookParameterIndex.objects.filter(parametername__icontains=search_query)
        else:
            parameters = WebhookParameterIndex.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(parameters, page_size)
        paginated_parameters = paginator.get_page(page)
        serializer = WebhookParameterIndexSerializer(paginated_parameters, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_parameters.number,
            'total_items': paginator.count
        })

class WebhookParameterIndexCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        indexnumber = data.get('indexnumber')
        parametername = data.get('parametername')

        if WebhookParameterIndex.objects.filter(indexnumber=indexnumber, parametername=parametername).exists():
            return Response({"error": "A record with this index number and parameter name already exists."}, status=status.HTTP_400_BAD_REQUEST)

        data['created_date'] = datetime.datetime.now().isoformat()
        serializer = WebhookParameterIndexSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WebhookParameterIndexUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        webhookparameter_id = data.get('webhookparameter_id')

        if not webhookparameter_id:
            return Response({'detail': 'webhookparameter_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the current parameter object
        parameter = get_object_or_404(WebhookParameterIndex, pk=webhookparameter_id)

        indexnumber = data.get('indexnumber')
        parametername = data.get('parametername')

        # Check if another record with the same indexnumber and parametername exists
        if WebhookParameterIndex.objects.filter(indexnumber=indexnumber, parametername=parametername).exclude(pk=webhookparameter_id).exists():
            return Response({"error": "A record with this index number and parameter name already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the parameter object with the new data
        data['update_date'] = datetime.datetime.now().isoformat()
        serializer = WebhookParameterIndexSerializer(parameter, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

