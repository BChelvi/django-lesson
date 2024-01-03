from rest_framework import serializers, viewsets, permissions
from zoo.models import Keeper


class KeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keeper
        fields = ['id', 'name', 'email', 'hire_date']


class KeeperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Keeper.objects.all()
    serializer_class = KeeperSerializer
    permission_classes = [permissions.IsAuthenticated]
