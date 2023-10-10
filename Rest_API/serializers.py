from rest_framework import serializers
from . models import student



class SudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['id','name','marks']