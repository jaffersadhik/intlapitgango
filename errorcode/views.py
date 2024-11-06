from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import ErrorcodeAccount
from .serializers import ErrorcodeAccountSerializer
import base64
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

class ErrorcodeAccountListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            accounts = ErrorcodeAccount.objects.filter(accountname__icontains=search_query)
        else:
            accounts = ErrorcodeAccount.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = ErrorcodeAccountSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class ErrorcodeAccountCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()

        # Set created_date to the current timestamp
        data['created_date'] = datetime.now().isoformat()

        try:
            # Decode Base64-encoded accountname if present
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname

        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing combination of accountname 
        existing_entry = ErrorcodeAccount.objects.filter(
        accountname=data.get('accountname'),
        errorcode=data.get('errorcode'),
        platformerrorcode=data.get('platformerrorcode'),
        description=data.get('description'),
        status=data.get('status')
        ).first()


        if existing_entry:
            return Response({"error": "Combination of accountname and pricepersms already exists."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = ErrorcodeAccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ErrorcodeAccountUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Set the current timestamp for update_date

        errorcode_id = data.get('errorcode_id')

        if not errorcode_id:
            return Response({'detail': 'errorcode_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        account = ErrorcodeAccount.objects.filter(pk=errorcode_id).first()

        if not account:
            return Response({'detail': 'ErrorcodeAccount not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Decode Base64-encoded accountname if present
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname

        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing combination of accountname and pricepersms, excluding the current account
        existing_entry = ErrorcodeAccount.objects.filter(
            accountname=data.get('accountname'),
            errorcode=data.get('errorcode'),
            platformerrorcode=data.get('platformerrorcode'),
            description=data.get('description'),
            status=data.get('status')
            ).exclude(pk=errorcode_id).first()

        if existing_entry:
            return Response({"error": "Combination of accountname and pricepersms already exists."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = ErrorcodeAccountSerializer(account, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import ErrorcodeCarrier
from .serializers import ErrorcodeCarrierSerializer

class ErrorcodeCarrierListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            carriers = ErrorcodeCarrier.objects.filter(carriername__icontains=search_query)
        else:
            carriers = ErrorcodeCarrier.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(carriers, page_size)
        paginated_carriers = paginator.get_page(page)
        serializer = ErrorcodeCarrierSerializer(paginated_carriers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_carriers.number,
            'total_items': paginator.count
        })

class ErrorcodeCarrierCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        # Set created_date to the current timestamp
        data['created_date'] = datetime.now().isoformat()

        
        # Check for existing combination of accountname, errorcode, and carriername
        existing_entry = ErrorcodeCarrier.objects.filter(
            errorcode=data.get('errorcode'),
            carriername=data.get('carriername'),
            platformerrorcode=data.get('platformerrorcode'),
            status=data.get('status')
        ).first()

        if existing_entry:
            return Response({"error": "Combination of accountname, errorcode, and carriername already exists."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Validate and save data using the serializer
        serializer = ErrorcodeCarrierSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ErrorcodeCarrierUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        errorcode_id = data.get('errorcode_id')

        if not errorcode_id:
            return Response({'detail': 'errorcode_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        carrier = ErrorcodeCarrier.objects.filter(pk=errorcode_id).first()

        if not carrier:
            return Response({'detail': 'ErrorcodeCarrier not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ErrorcodeCarrierSerializer(carrier, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from .models import ErrorcodePlatform
from .serializers import ErrorcodePlatformSerializer

class ErrorcodePlatformListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')
        all_data = request.GET.get('all', 'false').lower() == 'true'  # Check for all=true

        if search_query:
            platforms = ErrorcodePlatform.objects.filter(description__icontains=search_query)
        else:
            platforms = ErrorcodePlatform.objects.all().order_by('-update_date', '-created_date')

        if all_data:
            # If 'all=true', return all data without pagination
            serializer = ErrorcodePlatformSerializer(platforms, many=True)
            return Response({
                'data': serializer.data,
                'total_items': platforms.count()
            })
        else:
            # Use pagination
            paginator = Paginator(platforms, page_size)
            paginated_platforms = paginator.get_page(page)
            serializer = ErrorcodePlatformSerializer(paginated_platforms, many=True)

            return Response({
                'data': serializer.data,
                'total_pages': paginator.num_pages,
                'current_page': paginated_platforms.number,
                'total_items': paginator.count
            })

class ErrorcodePlatformCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        serializer = ErrorcodePlatformSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ErrorcodePlatformUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        errorcode_id = data.get('errorcode_id')

        if not errorcode_id:
            return Response({'detail': 'errorcode_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        platform = ErrorcodePlatform.objects.filter(pk=errorcode_id).first()

        if not platform:
            return Response({'detail': 'ErrorcodePlatform not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ErrorcodePlatformSerializer(platform, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .models import ErrorcodeCustomer
from .serializers import ErrorcodeCustomerSerializer
class ErrorcodeCustomerListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            customers = ErrorcodeCustomer.objects.filter(customername__icontains=search_query)
        else:
            customers = ErrorcodeCustomer.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(customers, page_size)
        paginated_customers = paginator.get_page(page)
        serializer = ErrorcodeCustomerSerializer(paginated_customers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_customers.number,
            'total_items': paginator.count
        })

class ErrorcodeCustomerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        # Set created_date to the current timestamp
        data['created_date'] = datetime.now().isoformat()

        # Decode Base64-encoded customername if present
       

        # Check for existing combination of customername
        existing_entry = ErrorcodeCustomer.objects.filter(
            customername=data.get('customername'),
            errorcode=data.get('errorcode'),
            platformerrorcode=data.get('platformerrorcode'),
            description=data.get('description'),
            status=data.get('status')
        ).first()

        if existing_entry:
            return Response({"error": "Combination of customername and errorcode already exists."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = ErrorcodeCustomerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ErrorcodeCustomerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Set the current timestamp for update_date

        errorcode_id = data.get('errorcode_id')

        if not errorcode_id:
            return Response({'error': 'errorcode_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        customer = ErrorcodeCustomer.objects.filter(pk=errorcode_id).first()

        if not customer:
            return Response({'error': 'ErrorcodeCustomer not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Decode Base64-encoded customername if present
        
        # Check for existing combination of customername, excluding the current customer
        existing_entry = ErrorcodeCustomer.objects.filter(
            customername=data.get('customername'),
            errorcode=data.get('errorcode'),
            platformerrorcode=data.get('platformerrorcode'),
            description=data.get('description'),
            status=data.get('status')
        ).exclude(pk=errorcode_id).first()

        if existing_entry:
            return Response({"error": "Combination of customername and errorcode already exists."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = ErrorcodeCustomerSerializer(customer, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



from .models import ErrorcodeSmsServiceProvider
from .serializers import ErrorcodeSmsServiceProviderSerializer

class ErrorcodeSmsServiceProviderListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            providers = ErrorcodeSmsServiceProvider.objects.filter(smsserviceprovider__icontains=search_query)
        else:
            providers = ErrorcodeSmsServiceProvider.objects.all().order_by('-update_date', '-created_date')

        paginator = Paginator(providers, page_size)
        paginated_providers = paginator.get_page(page)
        serializer = ErrorcodeSmsServiceProviderSerializer(paginated_providers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_providers.number,
            'total_items': paginator.count
        })

class ErrorcodeSmsServiceProviderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()  # Set created_date to the current timestamp

        # Validation: Check if a similar record already exists
        if ErrorcodeSmsServiceProvider.objects.filter(
            errorcode=data.get('errorcode'),
            platformerrorcode=data.get('platformerrorcode'),
            smsserviceprovider=data.get('smsserviceprovider'),
            status=data.get('status')


        ).exists():
            return Response(
                {'error': 'An Errorcode SMS Service Provider with the same errorcode, platformerrorcode, and smsserviceprovider already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ErrorcodeSmsServiceProviderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ErrorcodeSmsServiceProviderUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()  # Set the current timestamp for update_date

        errorcode_id = data.get('errorcode_id')
        if not errorcode_id:
            return Response({'detail': 'errorcode_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        provider = ErrorcodeSmsServiceProvider.objects.filter(pk=errorcode_id).first()
        if not provider:
            return Response({'detail': 'ErrorcodeSmsServiceProvider not found.'}, status=status.HTTP_404_NOT_FOUND)

       

        serializer = ErrorcodeSmsServiceProviderSerializer(provider, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)