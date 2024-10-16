from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import uuid
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q  # For complex queries
from .models import IPCheck, MNCMCCCheck, InvoiceType, Protocol, RouteCheck, RouteType, SenderIdCheck, SmsType, Status, PriceCheck
from .serializers import IPCheckSerializer, MNCMCCCheckSerializer, InvoiceTypeSerializer, ProtocolSerializer, RouteCheckSerializer, RouteTypeSerializer, SenderIdCheckSerializer, SmsTypeSerializer, StatusSerializer, PriceCheckSerializer

# IPCheck Views
class IPCheckListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            ip_checks = IPCheck.objects.filter(
                Q(type__icontains=search_query)  
            )
        else:
            ip_checks = IPCheck.objects.all()

        paginator = Paginator(ip_checks, page_size)
        paginated_ip_checks = paginator.get_page(page)
        serializer = IPCheckSerializer(paginated_ip_checks, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_ip_checks.number,
            'total_items': paginator.count
        })

class IPCheckCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = IPCheckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IPCheckUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        ipcheck_id = data.get('ipcheck_id')
        if not ipcheck_id:
            return Response({'detail': 'ipcheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        ip_check = get_object_or_404(IPCheck, pk=ipcheck_id)
        serializer = IPCheckSerializer(ip_check, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# MNCMCCCheck Views
class MNCMCCCheckListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            mncmcc_checks = MNCMCCCheck.objects.filter(
                Q(type__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            mncmcc_checks = MNCMCCCheck.objects.all()

        paginator = Paginator(mncmcc_checks, page_size)
        paginated_mncmcc_checks = paginator.get_page(page)
        serializer = MNCMCCCheckSerializer(paginated_mncmcc_checks, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_mncmcc_checks.number,
            'total_items': paginator.count
        })

class MNCMCCCheckCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = MNCMCCCheckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MNCMCCCheckUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        senderidcheck_id = data.get('senderidcheck_id')
        if not senderidcheck_id:
            return Response({'detail': 'senderidcheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mncmcc_check = get_object_or_404(MNCMCCCheck, pk=senderidcheck_id)
        serializer = MNCMCCCheckSerializer(mncmcc_check, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# InvoiceType Views
class InvoiceTypeListView(APIView):
    def get(self, request):
        # Retrieve page number, page size, and search query from the request
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')  # Get search query

        # Fetch all invoice types, filtered by search if provided
        if search_query:
            invoice_types = InvoiceType.objects.filter(
                Q(invoicetype__icontains=search_query)
            )
        else:
            invoice_types = InvoiceType.objects.all()

        # Paginate the queryset
        paginator = Paginator(invoice_types, page_size)
        paginated_invoice_types = paginator.get_page(page)

        # Serialize the data
        serializer = InvoiceTypeSerializer(paginated_invoice_types, many=True)

        # Return paginated data and additional pagination info
        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_invoice_types.number,
            'total_items': paginator.count
        })

class InvoiceTypeCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = InvoiceTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceTypeUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        invoicetype_id = data.get('invoicetype_id')
        if not invoicetype_id:
            return Response({'detail': 'invoicetype_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        invoice_type = get_object_or_404(InvoiceType, pk=invoicetype_id)
        serializer = InvoiceTypeSerializer(invoice_type, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Protocol Views
class ProtocolListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            protocols = Protocol.objects.filter(
                Q(some_field__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            protocols = Protocol.objects.all()

        paginator = Paginator(protocols, page_size)
        paginated_protocols = paginator.get_page(page)
        serializer = ProtocolSerializer(paginated_protocols, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_protocols.number,
            'total_items': paginator.count
        })


class ProtocolCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = ProtocolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProtocolUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        senderidcheck_id = data.get('senderidcheck_id')
        if not senderidcheck_id:
            return Response({'detail': 'senderidcheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        protocol = get_object_or_404(Protocol, pk=senderidcheck_id)
        serializer = ProtocolSerializer(protocol, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RouteCheck Views
class RouteCheckListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            route_checks = RouteCheck.objects.filter(
                Q(type__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            route_checks = RouteCheck.objects.all()

        paginator = Paginator(route_checks, page_size)
        paginated_route_checks = paginator.get_page(page)
        serializer = RouteCheckSerializer(paginated_route_checks, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_route_checks.number,
            'total_items': paginator.count
        })

class RouteCheckCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = RouteCheckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteCheckUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        routecheck_id = data.get('routecheck_id')
        if not routecheck_id:
            return Response({'detail': 'routecheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        route_check = get_object_or_404(RouteCheck, pk=routecheck_id)
        serializer = RouteCheckSerializer(route_check, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RouteType Views
class RouteTypeListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            route_types = RouteType.objects.filter(
                Q(type__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            route_types = RouteType.objects.all()

        paginator = Paginator(route_types, page_size)
        paginated_route_types = paginator.get_page(page)
        serializer = RouteTypeSerializer(paginated_route_types, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_route_types.number,
            'total_items': paginator.count
        })

class RouteTypeCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = RouteTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteTypeUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        routetype_id = data.get('routetype_id')
        if not routetype_id:
            return Response({'detail': 'routetype_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        route_type = get_object_or_404(RouteType, pk=routetype_id)
        serializer = RouteTypeSerializer(route_type, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# SenderIdCheck Views
class SenderIdCheckListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            sender_id_checks = SenderIdCheck.objects.filter(
                Q(type__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            sender_id_checks = SenderIdCheck.objects.all()

        paginator = Paginator(sender_id_checks, page_size)
        paginated_sender_id_checks = paginator.get_page(page)
        serializer = SenderIdCheckSerializer(paginated_sender_id_checks, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_sender_id_checks.number,
            'total_items': paginator.count
        })

class SenderIdCheckCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = SenderIdCheckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SenderIdCheckUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        senderidcheck_id = data.get('senderidcheck_id')
        if not senderidcheck_id:
            return Response({'detail': 'senderidcheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        sender_id_check = get_object_or_404(SenderIdCheck, pk=senderidcheck_id)
        serializer = SenderIdCheckSerializer(sender_id_check, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# SmsType Views
class SmsTypeListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            sms_types = SmsType.objects.filter(
                Q(smstype__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            sms_types = SmsType.objects.all()

        paginator = Paginator(sms_types, page_size)
        paginated_sms_types = paginator.get_page(page)
        serializer = SmsTypeSerializer(paginated_sms_types, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_sms_types.number,
            'total_items': paginator.count
        })

class SmsTypeCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = SmsTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SmsTypeUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        smstype_id = data.get('smstype_id')
        if not smstype_id:
            return Response({'detail': 'smstype_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        sms_type = get_object_or_404(SmsType, pk=smstype_id)
        serializer = SmsTypeSerializer(sms_type, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Status Views
class StatusListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            statuses = Status.objects.filter(
                Q(type__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            statuses = Status.objects.all()

        paginator = Paginator(statuses, page_size)
        paginated_statuses = paginator.get_page(page)
        serializer = StatusSerializer(paginated_statuses, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_statuses.number,
            'total_items': paginator.count
        })

class StatusCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = StatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        senderidcheck_id = data.get('senderidcheck_id')
        if not senderidcheck_id:
            return Response({'detail': 'senderidcheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        status_obj = get_object_or_404(Status, pk=senderidcheck_id)
        serializer = StatusSerializer(status_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PriceCheck Views
class PriceCheckListView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            price_checks = PriceCheck.objects.filter(
                Q(type__icontains=search_query)  # Replace 'some_field' with actual searchable fields
            )
        else:
            price_checks = PriceCheck.objects.all()

        paginator = Paginator(price_checks, page_size)
        paginated_price_checks = paginator.get_page(page)
        serializer = PriceCheckSerializer(paginated_price_checks, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_price_checks.number,
            'total_items': paginator.count
        })

class PriceCheckCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = PriceCheckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceCheckUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        pricecheck_id = data.get('pricecheck_id')
        if not pricecheck_id:
            return Response({'detail': 'pricecheck_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        price_check = get_object_or_404(PriceCheck, pk=pricecheck_id)
        serializer = PriceCheckSerializer(price_check, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .models import SmsServiceProvider
from .serializers import SmsServiceProviderSerializer  # Make sure to create a serializer for your model

class SmsServiceProviderListView(APIView):
    def get(self, request):
        # Retrieve query parameters
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')
        all_data = request.GET.get('all', 'false').lower() == 'true'  # Check if 'all' parameter is true

        if search_query:
            providers = SmsServiceProvider.objects.filter(
                Q(smsserviceprovidername__icontains=search_query)
            )
        else:
            providers = SmsServiceProvider.objects.all()

        if all_data:
            # If 'all' is true, return all data without pagination
            serializer = SmsServiceProviderSerializer(providers, many=True)
            return Response({
                'data': serializer.data,
                'total_items': providers.count()
            })
        else:
            # Otherwise, paginate the results
            paginator = Paginator(providers, page_size)
            paginated_providers = paginator.get_page(page)
            serializer = SmsServiceProviderSerializer(paginated_providers, many=True)

            return Response({
                'data': serializer.data,
                'total_pages': paginator.num_pages,
                'current_page': paginated_providers.number,
                'total_items': paginator.count
            })

class SmsServiceProviderCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        smsserviceprovidername = data.get('smsserviceprovidername', None)
        
        # Check if the provider name already exists
        if SmsServiceProvider.objects.filter(smsserviceprovidername=smsserviceprovidername).exists():
            return Response(
                {"error": "Sms Service Provider with this name already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Proceed with serializer validation and saving if name does not exist
        serializer = SmsServiceProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SmsServiceProviderUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        provider_name = data.get('smsserviceprovidername')
        if not provider_name:
            return Response({'detail': 'smsserviceprovidername is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        provider = get_object_or_404(SmsServiceProvider, smsserviceprovidername=provider_name)
        serializer = SmsServiceProviderSerializer(provider, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)