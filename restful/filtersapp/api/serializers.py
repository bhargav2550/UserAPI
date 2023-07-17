from rest_framework import serializers
from filtersapp.models import users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = "__all__"