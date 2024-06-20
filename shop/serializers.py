from .models import Bikes
from rest_framework import serializers
from rest_framework import serializers
from .models import Customer, Sale, Bikes

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address']

class BikesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bikes
        fields = [
            'name',
            'size',
            'color',
            'description',
            'full_description',
            'price',
            'image',
            'age_category',
            'bike_categories',
        ]

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikes
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address']

class SaleSerializer(serializers.ModelSerializer):
    bike = BikesSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    sale_date = serializers.DateField(source='sale_date.date', read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'bike', 'customer', 'quantity', 'sale_date', 'total_price']
