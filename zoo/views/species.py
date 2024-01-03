from rest_framework import serializers, viewsets, permissions
from zoo.models import Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'name', 'description', 'conservation_status', 'animals']


class SpeciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = [permissions.IsAuthenticated]
