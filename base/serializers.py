from rest_framework import serializers
from .models import Movie,Actor,Relationship

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'release_D',
            'no_of_votes'
        )


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'name',
            'dob'
        )


class RelationshipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = (
            'movie',
            'actor',
        )