from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import uuid
from datetime import datetime
from .models import Country, MncMcc, MncMccPrefix, WorldTimezone
from .serializers import CountrySerializer, MncMccSerializer, MncMccPrefixSerializer, WorldTimezoneSerializer
from django.utils import timezone

# Country Views
class CountryListView(APIView):
    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

class CountryCreateView(APIView):
    def post(self, request):
        if isinstance(request.data, list):
            created_countries = []
            for country_data in request.data:
                data = country_data.copy()
                data['created_date'] = datetime.now().isoformat()  # Set created_date
                serializer = CountrySerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()
                    created_countries.append(serializer.data)  # Collect created country data
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(created_countries, status=status.HTTP_201_CREATED)

        return Response({"error": "Expected a list of country objects."}, status=status.HTTP_400_BAD_REQUEST)
class CountryUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        country_id = data.get('country_id')
        if not country_id:
            return Response({'detail': 'country_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        country = get_object_or_404(Country, pk=country_id)
        serializer = CountrySerializer(country, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# MncMcc Views
class MncMccListView(APIView):
    def get(self, request):
        mncmccs = MncMcc.objects.all()
        serializer = MncMccSerializer(mncmccs, many=True)
        return Response(serializer.data)


    
class MncMccCreateView(APIView):
    def post(self, request):
        # Load the JSON data from the request body
        data = request.data

        # Prepare a list to hold the MncMcc instances to be created
        mnc_mcc_objects = []

        for entry in data:
            # Set created_date to today's date if not provided
            created_date = entry.get('created_date', timezone.now())

            # Create a new instance of MncMcc for each entry in the JSON
            mnc_mcc = MncMcc(
                mcc=entry.get('mcc'),
                mnc=entry.get('mnc'),
                networkoperatorname=entry.get('networkoperatorname'),
                dial_in_code=entry.get('dial_in_code'),
                created_date=created_date,  # Use today's date if not provided
                update_date=entry.get('update_date'),  # Optional
            )
            mnc_mcc_objects.append(mnc_mcc)

        # Bulk create the MncMcc instances in the database
        MncMcc.objects.bulk_create(mnc_mcc_objects)

        return Response({'message': 'Data added successfully'}, status=status.HTTP_201_CREATED)

class MncMccUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        mncmcc_id = data.get('mncmcc_id')
        if not mncmcc_id:
            return Response({'detail': 'mncmcc_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mncmcc = get_object_or_404(MncMcc, pk=mncmcc_id)
        serializer = MncMccSerializer(mncmcc, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# MncMccPrefix Views
class MncMccPrefixListView(APIView):
    def get(self, request):
        mncmcc_prefixes = MncMccPrefix.objects.all()
        serializer = MncMccPrefixSerializer(mncmcc_prefixes, many=True)
        return Response(serializer.data)

class MncMccPrefixCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['update_date'] = datetime.now().isoformat()
        serializer = MncMccPrefixSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MncMccPrefixUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        mccmncprefix_id = data.get('mccmncprefix_id')
        if not mccmncprefix_id:
            return Response({'detail': 'mccmncprefix_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        mncmcc_prefix = get_object_or_404(MncMccPrefix, pk=mccmncprefix_id)
        serializer = MncMccPrefixSerializer(mncmcc_prefix, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# WorldTimezone Views
class WorldTimezoneListView(APIView):
    def get(self, request):
        timezones = WorldTimezone.objects.all()
        serializer = WorldTimezoneSerializer(timezones, many=True)
        return Response(serializer.data)

class WorldTimezoneCreateView(APIView):
    def post(self, request):
        # Check if the incoming data is a list (multiple time zones)
        if isinstance(request.data, list):
            # Create a list to store responses for each time zone
            response_data = []
            for data in request.data:
                data['created_date'] = datetime.now().isoformat()
                serializer = WorldTimezoneSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            # Handle the case for a single time zone (dictionary)
            data = request.data.copy()
            data['created_date'] = datetime.now().isoformat()
            serializer = WorldTimezoneSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorldTimezoneUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        timezone_id = data.get('timezone_id')
        if not timezone_id:
            return Response({'detail': 'timezone_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        timezone = get_object_or_404(WorldTimezone, pk=timezone_id)
        serializer = WorldTimezoneSerializer(timezone, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
