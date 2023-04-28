from rest_framework import serializers
from .models import Movie,Review

class MovieListSerializer(serializers.ModelSerializer):
    review_set = serializers.PrimaryKeyRelatedField(many=True,read_onlt=True)
    class Meta:
        model = Movie
        fields="__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meata:
        model = Movie
        fields="__all__"
        read_only_fileds=('movie',)

