from rest_framework import serializers
from .models import User, Investment, Bill

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investment
        fields = ['id', 'user', 'investment_amount', 'fee_percentage', 'investment_date', 'up_front_payed']


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'user', 'bill_type', 'status', 'bill_date']