from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_rating']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'movie']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # Hide password for get request
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # Hashing the password before save overwriting the create method for ModelSerializer
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
