from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from zoo.models import Animal
from zoo.views import ZoneSerializer


class AnimalSerializer(serializers.ModelSerializer):
    zone_extended = ZoneSerializer(source="zone", read_only=True)
    class Meta:
        model = Animal
        fields = ['id', 'name', 'birth_date', 'species', 'diet', 'DIET_CHOICES', 'zone', 'zone_extended']


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=True,
        methods=["POST"]
    )
    def change_zone(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk)
        new_zone_id = request.data.get('zone_id')
        animal.zone = new_zone_id
        animal.save()

        notify_response = animal.zone.keeper.notify_animal_change(animal)

        if notify_response:
            return Response(status=status)
        return Response(status=status.HTTP_400_BAD_REQUEST)
