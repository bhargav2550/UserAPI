from django.shortcuts import render
from django.http import response,JsonResponse
from .models import users
from django.views.decorators.http import require_GET
import requests
# Create your views here.

@require_GET
def user_search(request):
    username = request.GET.get("first_name")

    if not username:
        return JsonResponse({'error': 'Missing query parameter first_name'}, status=400)
    
    matching_users = users.objects.filter(first_name__istartswith = username)

    if matching_users.exists():
        users_data = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                       'age': user.age, 'gender': user.gender, 'email': user.email,
                       'phone': user.phone, 'birth_date': user.birth_date}
                      for user in matching_users]
        return JsonResponse(users_data, safe=False)
    
    response = requests.get(f'https://dummyjson.com/users/search?q={username}')
    if response.status_code == 200:
        external_users = response.json()
        for external_user in external_users["users"]:
            users.objects.create(first_name=external_user["firstName"], last_name=external_user['lastName'],
                            age=external_user['age'], gender=external_user['gender'], email=external_user['email'],
                            phone=external_user['phone'], birth_date=external_user['birthDate'])
        return JsonResponse(external_users, safe=False)
    else:
        return JsonResponse({'error': 'Error retrieving users from the external API'}, status=500)


