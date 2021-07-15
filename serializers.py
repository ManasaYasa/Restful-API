from rest_framework import serializers
from .models import MovieData

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True) #use_url tell that image uses a path to store images

    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
