import django_filters
from .models import Offer

class OfferFilter(django_filters.FilterSet):
    class Meta:
        model = Offer
        fields = ['car_brand', 'car_model', 'fuel_type']