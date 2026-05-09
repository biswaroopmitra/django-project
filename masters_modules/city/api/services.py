from django.core.paginator import Paginator
from city.models.city_model import City


class CityService:
    @staticmethod
    def create_city(data):
        """Create a new city record."""
        city = City.objects.create(
            name=data.get('name'),
            code=data.get('code'),
            active=data.get('active', True)
        )
        return city

    @staticmethod
    def update_city(city_id, data):
        """Update an existing city record."""
        try:
            city = City.objects.get(id=city_id)
            city.name = data.get('name', city.name)
            city.code = data.get('code', city.code)
            city.active = data.get('active', city.active)
            city.save()
            return city
        except City.DoesNotExist:
            return None

    @staticmethod
    def get_city(city_id):
        """Retrieve a single city by ID."""
        try:
            return City.objects.get(id=city_id)
        except City.DoesNotExist:
            return None

    @staticmethod
    def get_city_by_name(name):
        """Retrieve a city by name."""
        try:
            return City.objects.get(name=name)
        except City.DoesNotExist:
            return None

    @staticmethod
    def list_cities(page=1, page_size=10):
        """List all cities with pagination."""
        cities = City.objects.all().order_by('-created_at')
        paginator = Paginator(cities, page_size)
        
        try:
            page_obj = paginator.page(page)
        except:
            page_obj = paginator.page(1)
        
        return {
            'cities': page_obj.object_list,
            'total_count': paginator.count,
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous()
        }

    @staticmethod
    def delete_city(city_id):
        """Delete a city record."""
        try:
            city = City.objects.get(id=city_id)
            city.delete()
            return True
        except City.DoesNotExist:
            return False
