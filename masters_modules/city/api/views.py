from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from city.api.serializer import CitySerializer
from city.api.services import CityService


class CityListCreateView(APIView):
    """
    Endpoint: GET /api/cities/ - List all cities with pagination
    Endpoint: POST /api/cities/ - Create a new city
    """

    def get(self, request):
        """List all cities with pagination."""
        page = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 10)

        try:
            page = int(page)
            page_size = int(page_size)
        except ValueError:
            page = 1
            page_size = 10

        result = CityService.list_cities(page=page, page_size=page_size)
        
        serializer = CitySerializer(result['cities'], many=True)
        return Response({
            'status': 'success',
            'data': serializer.data,
            'pagination': {
                'current_page': result['current_page'],
                'total_pages': result['total_pages'],
                'total_count': result['total_count'],
                'has_next': result['has_next'],
                'has_previous': result['has_previous']
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new city."""
        serializer = CitySerializer(data=request.data)
        
        if serializer.is_valid():
            city = CityService.create_city(serializer.validated_data)
            response_serializer = CitySerializer(city)
            return Response({
                'status': 'success',
                'message': 'City created successfully',
                'data': response_serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'status': 'error',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class CityDetailView(APIView):
    """
    Endpoint: GET /api/cities/<id>/ - Retrieve a single city
    Endpoint: PUT/PATCH /api/cities/<id>/ - Update a city
    Endpoint: DELETE /api/cities/<id>/ - Delete a city
    """

    def get(self, request, city_id):
        """Retrieve a single city by ID."""
        city = CityService.get_city(city_id)
        
        if not city:
            return Response({
                'status': 'error',
                'message': 'City not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitySerializer(city)
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, city_id):
        """Update a city (full update)."""
        city = CityService.get_city(city_id)
        
        if not city:
            return Response({
                'status': 'error',
                'message': 'City not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitySerializer(data=request.data, partial=False)
        
        if serializer.is_valid():
            updated_city = CityService.update_city(city_id, serializer.validated_data)
            response_serializer = CitySerializer(updated_city)
            return Response({
                'status': 'success',
                'message': 'City updated successfully',
                'data': response_serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': 'error',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, city_id):
        """Partial update a city."""
        city = CityService.get_city(city_id)
        
        if not city:
            return Response({
                'status': 'error',
                'message': 'City not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitySerializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            updated_city = CityService.update_city(city_id, serializer.validated_data)
            response_serializer = CitySerializer(updated_city)
            return Response({
                'status': 'success',
                'message': 'City updated successfully',
                'data': response_serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': 'error',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, city_id):
        """Delete a city."""
        success = CityService.delete_city(city_id)
        
        if not success:
            return Response({
                'status': 'error',
                'message': 'City not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        return Response({
            'status': 'success',
            'message': 'City deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


class CityDetailByNameView(APIView):
    """
    Endpoint: GET /api/cities/by-name/?name=<city_name> - Retrieve a city by name
    """

    def get(self, request):
        """Retrieve a city by name."""
        city_name = request.query_params.get('name')
        
        if not city_name:
            return Response({
                'status': 'error',
                'message': 'Name parameter is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        city = CityService.get_city_by_name(city_name)
        
        if not city:
            return Response({
                'status': 'error',
                'message': 'City not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitySerializer(city)
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_200_OK)