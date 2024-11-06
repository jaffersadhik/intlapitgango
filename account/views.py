from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Account, Company, Customer
from .serializers import AccountSerializer, CompanySerializer, CustomerSerializer
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
import base64
from rest_framework.permissions import IsAuthenticated
# ---- Account Views ----

class AccountListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all_accounts = request.GET.get('all', False)
        
        if all_accounts:
            accounts = Account.objects.all()
        else:
            page = request.GET.get('page', 1)
            page_size = request.GET.get('page_size', 10)
            search_query = request.GET.get('search', '')

            if search_query:
                accounts = Account.objects.filter(
                    Q(username__icontains=search_query) |  
                    Q(emailstatus__icontains=search_query)
                )
            else:
                accounts = Account.objects.all().order_by('-update_date', '-created_date')

            paginator = Paginator(accounts, page_size)
            paginated_accounts = paginator.get_page(page)
            serializer = AccountSerializer(paginated_accounts, many=True)

            return Response({
                'data': serializer.data,
                'total_pages': paginator.num_pages,
                'current_page': paginated_accounts.number,
                'total_items': paginator.count
            })

        # For all accounts
        serializer = AccountSerializer(accounts, many=True)
        return Response({
            'data': serializer.data,
        })

    
class AccountCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        required_fields = ['loginpassword', 'username',  'password', 'dial_in_code', 'currencycode', 'customer_id', 'ipcheck', 'mncmcccheck', 'pricecheck', 'protocol', 'routecheck', 'routetype', 'senderidcheck', 'smstype', 'status', 'timezone_id','errorcode_type','cluster']

        # Check for missing required fields
        for field in required_fields:
            if not data.get(field):
                return Response({field: f'{field.replace("_", " ").title()} is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Attempt to decode the Base64 encoded fields
        try:
            if 'loginpassword' in data:
                decoded_loginpassword = base64.b64decode(data['loginpassword']).decode('utf-8')
                data['loginpassword'] = decoded_loginpassword
            
            if 'username' in data:
                decoded_username = base64.b64decode(data['username']).decode('utf-8')
                data['username'] = decoded_username
            
            if 'password' in data:
                decoded_password = base64.b64decode(data['password']).decode('utf-8')
                data['password'] = decoded_password
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded value"}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing username or email
        if Account.objects.filter(username=data['username']).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        

        # Set creation and update date
        data['created_date'] = datetime.now().isoformat()
        data['update_date'] = datetime.now().isoformat()

        # Attempt to serialize and save the account data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    required_fields = ['loginpassword', 'username', 'password', 'dial_in_code', 'currencycode', 'customer_id', 'ipcheck', 'mncmcccheck', 'pricecheck', 'protocol', 'routecheck', 'routetype', 'senderidcheck', 'smstype', 'status', 'timezone_id','errorcode_type']

    def validate_and_decode(self, data):
        # Check for missing required fields
        for field in self.required_fields:
            if not data.get(field):
                return {field: f'{field.replace("_", " ").title()} is required'}, None
        
        # Attempt to decode the Base64 encoded fields
        try:
            for field in ['loginpassword', 'username', 'password']:
                if field in data:
                    decoded_value = base64.b64decode(data[field]).decode('utf-8')
                    data[field] = decoded_value
        except (base64.binascii.Error, UnicodeDecodeError):
            return {"error": "Invalid Base64-encoded value"}, None

        return None, data

    def post(self, request):
        data = request.data.copy()
        account_id = data.get('account_id')
        if not account_id:
            return Response({'detail': 'account_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate and decode data
        error, validated_data = self.validate_and_decode(data)
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        # Check if the username is already taken (excluding the current account)
        username = validated_data.get('username')
        if username and Account.objects.exclude(pk=account_id).filter(username=username).exists():
            return Response({'username': 'This username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        account = get_object_or_404(Account, pk=account_id)
        
        # Set the updated date
        validated_data['update_date'] = datetime.now().isoformat()

        # Attempt to serialize and save the account data
        serializer = AccountSerializer(account, data=validated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---- Company Views ----

class CompanyListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            companies = Company.objects.filter(
                Q(username__icontains=search_query) |  # Add fields to search
                Q(email__icontains=search_query)
            )
        else:
            companies = Company.objects.all().order_by('-update_date', '-create_date')

        paginator = Paginator(companies, page_size)
        paginated_companies = paginator.get_page(page)
        serializer = CompanySerializer(paginated_companies, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_companies.number,
            'total_items': paginator.count
        })

class CompanyCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        # Check for Base64 encoding and decode the username and password
        try:
            if 'username' in data:
                decoded_username = base64.b64decode(data['username']).decode('utf-8')
                data['username'] = decoded_username
            
            if 'password' in data:
                decoded_password = base64.b64decode(data['password']).decode('utf-8')
                data['password'] = decoded_password
        except(base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded value"}, status=status.HTTP_400_BAD_REQUEST)

        # Set creation date
        data['create_date'] = datetime.now().isoformat()

        # Validate if username or email already exists
        if Company.objects.filter(username=data.get('username')).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        if Company.objects.filter(email=data.get('email')).exists():
            return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and validate the data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CompanyUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        company_id = data.get('company_id')
        if not company_id:
            return Response({'detail': 'company_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        company = get_object_or_404(Company, pk=company_id)

        # Check for Base64 encoding and decode the username and password if present
        try:
            if 'username' in data:
                decoded_username = base64.b64decode(data['username']).decode('utf-8')
                data['username'] = decoded_username
            
            if 'password' in data:
                decoded_password = base64.b64decode(data['password']).decode('utf-8')
                data['password'] = decoded_password
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded value"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate if the new username or email already exists (excluding the current company)
        if 'username' in data and Company.objects.filter(username=data['username']).exclude(pk=company_id).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        if 'email' in data and Company.objects.filter(email=data['email']).exclude(pk=company_id).exists():
            return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Set update date
        data['update_date'] = datetime.now().isoformat()

        # Serialize and validate the data
        serializer = CompanySerializer(company, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ---- Customer Views ----

class CustomerListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all_customers = request.GET.get('all', False)

        if all_customers:
            customers = Customer.objects.all()
        else:
            page = request.GET.get('page', 1)
            page_size = request.GET.get('page_size', 10)
            search_query = request.GET.get('search', '')

            if search_query:
                customers = Customer.objects.filter(
                    Q(companyname__icontains=search_query) |  
                    Q(email__icontains=search_query) | 
                    Q(customername__icontains=search_query)
                )
            else:
                customers = Customer.objects.all().order_by('-customer_id')

            paginator = Paginator(customers, page_size)
            paginated_customers = paginator.get_page(page)
            serializer = CustomerSerializer(paginated_customers, many=True)

            return Response({
                'data': serializer.data,
                'total_pages': paginator.num_pages,
                'current_page': paginated_customers.number,
                'total_items': paginator.count
            })

        # For all customers
        serializer = CustomerSerializer(customers, many=True)
        return Response({
            'data': serializer.data,
        })


class CustomerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        required_fields = ['companyname', 'email', 'mobile', 'customername']
        
        # Check for missing required fields
        for field in required_fields:
            if not data.get(field):
                return Response({field: f'{field.replace("_", " ").title()} is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Attempt to decode the Base64 encoded password
            if 'loginpassword' in data:
                decoded_password = base64.b64decode(data['loginpassword']).decode('utf-8')
                data['loginpassword'] = decoded_password
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded password"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check for existing records with the same fields
        if Customer.objects.filter(companyname=data['companyname']).exists():
            return Response({
                "error": "A customer with the same companyname already exists."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if Customer.objects.filter(email=data['email']).exists():
            return Response({
                "error": "A customer with the same email already exists."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if Customer.objects.filter(mobile=data['mobile']).exists():
            return Response({
                "error": "A customer with the same mobile number already exists."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if Customer.objects.filter(customername=data['customername']).exists():
            return Response({
                "error": "A customer with the same customername already exists."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Set creation date
            data['created_date'] = datetime.now().isoformat()

            # Attempt to serialize and save the customer data
            serializer = CustomerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Catch any other exceptions and return a generic error message
            return Response({"error": "An error occurred while processing the request: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        customer_id = data.get('customer_id')

        # Check if customer_id is provided
        if not customer_id:
            return Response({'detail': 'customer_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the customer object
            customer = get_object_or_404(Customer, pk=customer_id)

            # Check for existing customers with the same attributes
            existing_customer = Customer.objects.filter(
                companyname=data.get('companyname', customer.companyname),
                email=data.get('email', customer.email),
                mobile=data.get('mobile', customer.mobile),
                customername=data.get('customername', customer.customername)
            ).exclude(pk=customer_id).first()

            if existing_customer:
                return Response({
                    "error": "A customer with the same companyname, email, mobile, and customername already exists."
                }, status=status.HTTP_400_BAD_REQUEST)

            # Attempt to decode the Base64 encoded password
            if 'loginpassword' in data:
                try:
                    decoded_password = base64.b64decode(data['loginpassword']).decode('utf-8')
                    data['loginpassword'] = decoded_password
                except (base64.binascii.Error, UnicodeDecodeError) as e:
                    return Response({"error": "Invalid Base64-encoded password"}, status=status.HTTP_400_BAD_REQUEST)

            # Update the 'update_date'
            data['update_date'] = datetime.now().isoformat()

            # Partial update using the serializer
            serializer = CustomerSerializer(customer, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Catch and return a generic error message
            return Response({"error": "An error occurred while updating the customer: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
