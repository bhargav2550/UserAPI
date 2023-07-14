
from rest_framework import generics
from filtersapp.api.serializers import UserSerializer
from filtersapp.models import users
from rest_framework.views import APIView



class UserView(generics.ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        #username = self.kwargs["first_name"]
        #return users.objects.filter(first_name__startswith = username)
        username = self.request.query_params.get('first_name')
        if username is not None:
            queryset = queryset.filter(users__first_name__startswith=username)
        return queryset
    

