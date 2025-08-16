from rest_framework import serializers
from .models import Task
from .models import Restaurant
from graphene_django_cruddals import DjangoModelCruddals

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CruddalsRestaurant(DjangoModelCruddals):
    class Meta:
        model = Restaurant