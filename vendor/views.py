from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Carrier,SMSC
from .serializers import CarrierSerializer,SMSCSerializer
import base64
from datetime import datetime
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

class CarrierListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all_data = request.GET.get('all', 'false').lower() == 'true'  # Check if 'all=true' is passed
        search_query = request.GET.get('search', '')
        
        # Filter carriers based on search query, if provided
        if search_query:
            carriers = Carrier.objects.filter(carriername__icontains=search_query)
        else:
            carriers = Carrier.objects.all().order_by('-update_date', '-created_date')

        # If 'all=true', return all carriers without pagination
        if all_data:
            serializer = CarrierSerializer(carriers, many=True)
            return Response({
                'data': serializer.data,
                'total_items': carriers.count()
            })
        
        # Otherwise, paginate the data
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        paginator = Paginator(carriers, page_size)
        paginated_carriers = paginator.get_page(page)
        serializer = CarrierSerializer(paginated_carriers, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_carriers.number,
            'total_items': paginator.count
        })


class CarrierCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = CarrierSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarrierUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        carriername = data.get('carriername')

        if not carriername:
            return Response({'detail': 'carrier_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        carrier = get_object_or_404(Carrier, pk=carriername)
        data['update_date'] = datetime.now().isoformat()
        serializer = CarrierSerializer(carrier, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SMSCListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all_smsc = request.GET.get('all', False)

        if all_smsc:
            smscs = SMSC.objects.all()
        else:
            page = request.GET.get('page', 1)
            page_size = request.GET.get('page_size', 10)
            search_query = request.GET.get('search', '')

            if search_query:
                smscs = SMSC.objects.filter(
                    Q(username__icontains=search_query) |  # Add fields you want to search
                    Q(smscid__icontains=search_query)
                )
            else:
                smscs = SMSC.objects.all().order_by('-update_date', '-created_date')

            paginator = Paginator(smscs, page_size)
            paginated_smsc = paginator.get_page(page)
            serializer = SMSCSerializer(paginated_smsc, many=True)

            return Response({
                'data': serializer.data,
                'total_pages': paginator.num_pages,
                'current_page': paginated_smsc.number,
                'total_items': paginator.count
            })

        # For all SMSCs
        serializer = SMSCSerializer(smscs, many=True)
        return Response({
            'data': serializer.data,
        })

class SMSCCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        
        # Attempt to decode the Base64 encoded username and password fields
        # for field in ['username', 'password']:
        #     if field in data:
        #         try:
        #             decoded_value = base64.b64decode(data[field]).decode('utf-8')
        #             data[field] = decoded_value
        #         except (base64.binascii.Error, UnicodeDecodeError):
        #             return Response({"error": f"Invalid Base64-encoded value for {field.replace('_', ' ').title()}"}, 
        #                             status=status.HTTP_400_BAD_REQUEST)

        # Check if smscid already exists
        smscid = data.get('smscid')
        if SMSC.objects.filter(smscid=smscid).exists():
            return Response({"error": "SMSC ID already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if username already exists
        # username = data.get('username')
        # if SMSC.objects.filter(username=username).exists():
        #     return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the created date
        data['created_date'] = datetime.now().isoformat()

        # Attempt to serialize and save the SMSC data
        serializer = SMSCSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SMSCUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        smscid = data.get('smscid')

        if not smscid:
            return Response({'detail': 'smscid is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        smsc = get_object_or_404(SMSC, pk=smscid)

        # Attempt to decode the Base64 encoded username and password fields
        for field in ['username', 'password']:
            if field in data:
                try:
                    decoded_value = base64.b64decode(data[field]).decode('utf-8')
                    data[field] = decoded_value
                except (base64.binascii.Error, UnicodeDecodeError) as e:
                    return Response({"error": f"Invalid Base64-encoded value for {field.replace('_', ' ').title()}"}, 
                                    status=status.HTTP_400_BAD_REQUEST)

        # Add the update date
        data['update_date'] = datetime.now().isoformat()
        
        serializer = SMSCSerializer(smsc, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





from .models import DataCenter, KannelHost, DCSmscid
from .serializers import DataCenterSerializer, KannelHostSerializer, DCSmscidSerializer
from datetime import datetime
import base64

# DataCenter Views
class DataCenterListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')
        all_data = request.GET.get('all', 'false').lower() == 'true'

        if search_query:
            datacenters = DataCenter.objects.filter(dcname__icontains=search_query)
        else:
            datacenters = DataCenter.objects.all().order_by('-update_date', '-created_date')

        if all_data:
            # Serialize all data centers without pagination
            serializer = DataCenterSerializer(datacenters, many=True)
            return Response({
                'data': serializer.data,
                'total_items': len(datacenters)
            })

        paginator = Paginator(datacenters, page_size)
        paginated_datacenters = paginator.get_page(page)
        serializer = DataCenterSerializer(paginated_datacenters, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_datacenters.number,
            'total_items': paginator.count
        })
class DataCenterCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = DataCenterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataCenterUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        dcname = data.get('dcname')

        if not dcname:
            return Response({'detail': 'dcname is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        datacenter = get_object_or_404(DataCenter, dcname=dcname)
        data['update_date'] = datetime.now().isoformat()
        serializer = DataCenterSerializer(datacenter, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# KannelHost Views
class KannelHostListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            kannel_hosts = KannelHost.objects.filter(kannelhostname__icontains=search_query)
        else:
            kannel_hosts = KannelHost.objects.all().order_by('-update_date', '-created_date')
        
        paginator = Paginator(kannel_hosts, page_size)
        paginated_kannel_hosts = paginator.get_page(page)
        serializer = KannelHostSerializer(paginated_kannel_hosts, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_kannel_hosts.number,
            'total_items': paginator.count
        })

class KannelHostCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = KannelHostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KannelHostUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        kannelhostname = data.get('kannelhostname')

        if not kannelhostname:
            return Response({'detail': 'kannelhostname is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        kannel_host = get_object_or_404(KannelHost, kannelhostname=kannelhostname)
        data['update_date'] = datetime.now().isoformat()
        serializer = KannelHostSerializer(kannel_host, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DCSmscid Views
class DCSmscidListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        if search_query:
            smscids = DCSmscid.objects.filter(username__icontains=search_query)
        else:
            smscids = DCSmscid.objects.all().order_by('-update_date', '-created_date')
        
        paginator = Paginator(smscids, page_size)
        paginated_smscids = paginator.get_page(page)
        serializer = DCSmscidSerializer(paginated_smscids, many=True)

        return Response({
            'data': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_smscids.number,
            'total_items': paginator.count
        })

class DCSmscidCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        try:
            
            
            if 'username' in data:
                decoded_username = base64.b64decode(data['username']).decode('utf-8')
                data['username'] = decoded_username
            
            if 'password' in data:
                decoded_password = base64.b64decode(data['password']).decode('utf-8')
                data['password'] = decoded_password
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            return Response({"error": "Invalid Base64-encoded value"}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing username or email
        if DCSmscid.objects.filter(username=data['username']).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        data['created_date'] = datetime.now().isoformat()
        serializer = DCSmscidSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DCSmscidUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        username = data.get('username')

        if not username:
            return Response({'detail': 'username is required for update.'}, status=status.HTTP_400_BAD_REQUEST)

        smscid = get_object_or_404(DCSmscid, username=username)
        data['update_date'] = datetime.now().isoformat()
        serializer = DCSmscidSerializer(smscid, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
