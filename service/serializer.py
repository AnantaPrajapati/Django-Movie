from rest_framework import serializers
from .models import Movie, User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


    def validate(self, data):
        if 'description' not in data or not data['description'].strip():
            raise serializers.ValidationError({'error': "description is must"})
        if 'movie_icon' not in data or not data['movie_icon'].strip():
            raise serializers.ValidationError({'error':'movie_icon should not be empty'})
        if 'release_date' not in data or not data['release_date'].strip():
            raise serializers.ValidationError({'error':'release_date should not be empty'})
        if 'movie_title' not in data or not data['movie_title'].strip():
            raise serializers.ValidationError({'error':'movie_title should not be empty'})
        if 'actor' not in data or not data['actor'].strip():
             raise serializers.ValidationError({'error':'actor should not be empty'})
        if 'country' not in data or not data['country'].strip():
            raise serializers.ValidationError({'error':'country should not be empty'})
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance 
        
