# takes in models
# and  serializes python objects to list or querysets 

from rest_framework.serializers import ModelSerializer

from base.models import Room



class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'