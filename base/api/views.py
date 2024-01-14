from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from base.api.serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)



@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    seri = RoomSerializer(rooms,many=True)
    return Response(seri.data)

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    seri = RoomSerializer(room,many=False)
    return Response(seri.data)
