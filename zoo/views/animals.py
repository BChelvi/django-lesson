from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from django_filters import rest_framework as filters

from zoo.models import Animal
from zoo.views import ZoneSerializer, SimplifiedZoneSerializer


class AnimalSerializer(serializers.ModelSerializer):
    zone_extended = ZoneSerializer(source="zone", read_only=True)
    zone_simplified = SimplifiedZoneSerializer(source="zone", read_only=True)
    class Meta:
        model = Animal
        fields = ['id', 'name', 'birth_date', 'species', 'diet', 'DIET_CHOICES', 'zone', 'zone_extended', 'zone_simplified']


class AnimalFilters(filters.FilterSet):
    class Meta:
        model = Animal
        fields = {
            'name': ['icontains', 'contains', 'exact'],
            'zone__name': ['icontains', 'contains', 'exact'],
            'zone__keepers__name': ['icontains', 'contains', 'exact'],
        }


class IsKeeperOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, animal):
        # Les requêtes en lecture sont toujours autorisées
        if request.method in SAFE_METHODS:
            return True
        # L'écriture n'est autorisée que si l'utilisateur actuel est le keeper de l'animal
        if not hasattr(request.user, 'keeper'):
            return False
        keepers = animal.zone.keepers
        return request.user.keeper in keepers.all() if keepers else False


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated, IsKeeperOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnimalFilters
    # filterset_fields = ['zone']

    @action(
        detail=True,
        methods=["POST"],
        # permission_classes=[IsKeeperOrReadOnly]
    )
    def change_zone(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk)
        new_zone_id = request.data.get('zone_id')
        animal.zone_id = new_zone_id
        animal.save()

        # notify_response = animal.zone.keeper.notify_animal_change(animal)

        # if notify_response:
        #     return Response(status=status)
        return Response(status=status.HTTP_400_BAD_REQUEST)
