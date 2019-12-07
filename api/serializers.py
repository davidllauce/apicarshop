# score/serializers.py
from rest_framework import serializers

from api.models import Score


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('usuario', 'email', 'score')
