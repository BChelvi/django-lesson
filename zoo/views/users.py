from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from zoo.views import GroupSerializer



class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups_extended = GroupSerializer(source="groups", read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', "groups_extended"]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()#.order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=True,
        methods=["GET"]
    )
    def send_mail(self, request, pk):
        user = get_object_or_404(pk=pk)

        return Response(status=status.HTTP_400_BAD_REQUEST)




class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
