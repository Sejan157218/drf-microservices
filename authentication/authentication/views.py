from rest_framework import generics
from users.models import UserList
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = '__all__'


class AllUser(generics.ListAPIView):
    queryset = UserList.objects.all()
    serializer_class = UserSerializer
