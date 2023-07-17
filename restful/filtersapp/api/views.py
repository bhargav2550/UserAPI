import requests
from rest_framework import generics
from filtersapp.api.serializers import UserSerializer
from filtersapp.models import users
from rest_framework.views import APIView
from django.http import JsonResponse


class UserView(generics.ListAPIView):

    queryset = users.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        #queryset = super().get_queryset()
        first_name = self.request.GET.get('first_name')
        if not first_name:
            return JsonResponse({"query parameter first_name is missing"},status = 200)
        if first_name:
            queryset = users.objects.filter(first_name__istartswith=first_name)
            if queryset:
                return queryset
            else:
                response = requests.get(f'https://dummyjson.com/users/search?q={first_name}')
                if response.status_code == 200:
                    external_users = response.json()
                    for external_user in external_users["users"]:
                        users.objects.create(first_name=external_user["firstName"], last_name=external_user['lastName'],
                                        age=external_user['age'], gender=external_user['gender'], email=external_user['email'],
                                        phone=external_user['phone'], Birth_date=external_user['birthDate'])
                    return JsonResponse(external_users, safe=False)
                else:
                    return JsonResponse({'error': 'Error retrieving users from the external API'}, status=500)
