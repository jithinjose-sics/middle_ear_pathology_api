from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import doctor
from .serializers import DoctorSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
def doctor_list_create_view(request):
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_api_view(request):
    mobile_number = request.data.get('mobile_number')
    password = request.data.get('password')

    if not mobile_number or not password:
        return Response({"error": "Please provide both 'mobile_number' and 'password.'"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, mobile_number=mobile_number, password=password)

    if user:
        # token, created = Token.objects.get_or_create(user=user)
        serializer = DoctorSerializer(user)
        #return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid mobile number or password."}, status=status.HTTP_401_UNAUTHORIZED)