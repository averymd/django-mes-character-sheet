from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from game_manager.models import Geist, Faction, Subrace
from game_manager.serializers import FactionSerializer, GeistSerializer, SubraceSerializer

class FactionList(APIView):
  """
  List all factions in a game.
  """
  def get(self, request, game_id, format=None):
    factions = Faction.objects.filter(game__id=game_id)
    serializer = FactionSerializer(factions, many=True)
    return Response(serializer.data)
    
class SubraceList(APIView):
  """
  List all subraces in a game.
  """
  def get(self, request, game_id, format=None):
    subraces = Subrace.objects.filter(game__id=game_id)
    serializer = SubraceSerializer(subraces, many=True)
    return Response(serializer.data)
    
class GameDetail(APIView):
  """
  Get the details for a game type.
  """
  def get(self, request, game_name, game_id, format=None):
    if game_name.lower() == 'geist':
      game = Geist.objects.select_related().get(pk=game_id)
      serializer = GeistSerializer(game, many=False)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)