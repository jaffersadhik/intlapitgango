from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Route, RouteAccount, RouteAccountMncmcc, RouteCustomer, RouteCustomerMncMcc,RouteShared, RouteSharedMncmcc
from .serializers import (
    RouteSerializer, RouteAccountSerializer, RouteAccountMncmccSerializer,
    RouteCustomerSerializer, RouteCustomerMncMccSerializer,RouteSharedSerializer, RouteSharedMncmccSerializer
)
import base64
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

# Route Views
class RouteListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        accounts = Route.objects.all().order_by('-update_date', '-created_date')
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = RouteSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class RouteCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        routename = data.get('routename')

        # Check if the routename already exists
        if Route.objects.filter(routename=routename).exists():
            return Response({'error': 'Route name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Add created_date to the data
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        route_id = data.get('route_id')

        if not route_id:
            return Response({'detail': 'route_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        route = get_object_or_404(Route, pk=route_id)

        data['update_date'] = datetime.now().isoformat()
        serializer = RouteSerializer(route, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RouteAccount Views
class RouteAccountListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        accounts = RouteAccount.objects.all().order_by('-update_date')
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = RouteAccountSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class RouteAccountCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError):
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)
        
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteAccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteAccountUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        
        routemapping_id = data.get('routemapping_id')

        if not routemapping_id:
            return Response({'detail': 'routemapping_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError):
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)

        account = get_object_or_404(RouteAccount, pk=routemapping_id)

        data['update_date'] = datetime.now().isoformat()
        serializer = RouteAccountSerializer(account, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RouteAccountMncmcc Views
class RouteAccountMncmccListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        accounts = RouteAccountMncmcc.objects.all().order_by('-update_date')
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = RouteAccountMncmccSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class RouteAccountMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError):
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteAccountMncmccSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteAccountMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        routemapping_id = data.get('routemapping_id')

        if not routemapping_id:
            return Response({'detail': 'routemapping_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if 'accountname' in data:
                decoded_accountname = base64.b64decode(data['accountname']).decode('utf-8')
                data['accountname'] = decoded_accountname
        except (base64.binascii.Error, UnicodeDecodeError):
            return Response({"error": "Invalid Base64-encoded accountname"}, status=status.HTTP_400_BAD_REQUEST)
        
        account = get_object_or_404(RouteAccountMncmcc, pk=routemapping_id)

        data['update_date'] = datetime.now().isoformat()
        serializer = RouteAccountMncmccSerializer(account, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RouteCustomer Views
class RouteCustomerListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        accounts = RouteCustomer.objects.all().order_by('-update_date')
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = RouteCustomerSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class RouteCustomerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteCustomerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteCustomerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        routemapping_id = data.get('routemapping_id')

        if not routemapping_id:
            return Response({'detail': 'routemapping_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        customer = get_object_or_404(RouteCustomer, pk=routemapping_id)

        data['update_date'] = datetime.now().isoformat()
        serializer = RouteCustomerSerializer(customer, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RouteCustomerMncMcc Views
class RouteCustomerMncmccListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        accounts = RouteCustomerMncMcc.objects.all().order_by('-update_date')
        paginator = Paginator(accounts, page_size)
        paginated_accounts = paginator.get_page(page)
        serializer = RouteCustomerMncMccSerializer(paginated_accounts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_accounts.number,
            'total_items': paginator.count
        })

class RouteCustomerMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteCustomerMncMccSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteCustomerMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        routemapping_id = data.get('routemapping_id')

        if not routemapping_id:
            return Response({'detail': 'routemapping_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        customer = get_object_or_404(RouteCustomerMncMcc, pk=routemapping_id)

        data['update_date'] = datetime.now().isoformat()
        serializer = RouteCustomerMncMccSerializer(customer, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# RouteShared Views
class RouteSharedListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Retrieve pagination parameters
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        
        # Retrieve search parameter
        search_query = request.GET.get('search', '')

        # Filter routes based on search query if provided
        routes = RouteShared.objects.all()
        if search_query:
            routes = routes.filter(route_name__icontains=search_query)  # Adjust the field name as needed

        # Paginate the filtered queryset
        paginator = Paginator(routes, page_size)
        paginated_routes = paginator.get_page(page)

        # Serialize the paginated data
        serializer = RouteSharedSerializer(paginated_routes, many=True)

        # Return the paginated response
        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_routes.number,
            'total_items': paginator.count
        })

class RouteSharedCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteSharedSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteSharedUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        routemapping_id = data.get('routemapping_id')

        if not routemapping_id:
            return Response({'detail': 'routemapping_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        route = get_object_or_404(RouteShared, pk=routemapping_id)
        data['update_date'] = datetime.now().isoformat()
        serializer = RouteSharedSerializer(route, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# RouteSharedMncmcc Views
class RouteSharedMncmccListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Retrieve pagination parameters
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        
        # Retrieve search parameter
        search_query = request.GET.get('search', '')

        # Filter routes based on search query if provided
        routes = RouteSharedMncmcc.objects.all()
        if search_query:
            routes = routes.filter(route_name__icontains=search_query)  # Adjust the field name as needed

        # Paginate the filtered queryset
        paginator = Paginator(routes, page_size)
        paginated_routes = paginator.get_page(page)

        # Serialize the paginated data
        serializer = RouteSharedMncmccSerializer(paginated_routes, many=True)

        # Return the paginated response
        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_routes.number,
            'total_items': paginator.count
        })

class RouteSharedMncmccCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = RouteSharedMncmccSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteSharedMncmccUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        routemapping_id = data.get('routemapping_id')

        if not routemapping_id:
            return Response({'detail': 'routemapping_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        route = get_object_or_404(RouteSharedMncmcc, pk=routemapping_id)
        data['update_date'] = datetime.now().isoformat()
        serializer = RouteSharedMncmccSerializer(route, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)