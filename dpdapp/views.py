from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CustomUserSerilizer, CustomDataSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model  
from .models import keyValue
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
User = get_user_model()

@api_view(["GET"])
def index(request):
    return Response({"Hello":"Hello world"})

@api_view(["GET","POST"])
def create_user(request):
    serializer = CustomUserSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"status":"success","message":"User successfully registered!","data":request.data}
        )
    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "POST"])
def store_data(request):
    if request.method == "POST":
        serializer = CustomDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "Data stored successfully."})
        return Response(serializer.errors, status=400)  # Return validation errors
    return Response({"message": "Invalid request method."}, status=405)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_store_data(request):
    if request.method == "GET":
        key = request.data.get('key')
        if key is None:
            return Response({"message": "Key parameter missing."}, status=400)  
        data_queryset = keyValue.objects.filter(key=key)
        serializer = CustomDataSerializer(data_queryset, many=True)
        return Response({"status": "success", "data": serializer.data})
    return Response({"message": "Invalid request method."}, status=405)


@api_view(["GET","PUT"])
@permission_classes([IsAuthenticated])
def update_store_data(request):
    key = request.data.get('key')
    if key is None:
        return Response({"message":"key parameter missing."},status=400)
    try:
            data_query = keyValue.objects.get(key=key, user=request.user)
    except keyValue.DoesNotExist:
            return Response({"message": "Data entry not found for the provided key."}, status=404)
    serializer = CustomDataSerializer(data_query, data=request.data)
    if request.method == "PUT":
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "Data updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Invalid request method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_store_data(request):
    key = request.data.get('key')
    if key is None:
        return Response({"message": "Key parameter missing."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        data_entry = keyValue.objects.get(key=key, user=request.user)
    except keyValue.DoesNotExist:
        return Response({"message": "Data entry not found for the provided key."}, status=status.HTTP_404_NOT_FOUND)
    data_entry.delete()
    return Response({"status": "success", "message": "Data entry deleted successfully."})


@api_view(["GET","POST"])
def login_user(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        user = authenticate(request, username= username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            headers = {"Authorization": f"token {access_token}"}
            return Response(
                {
                    "status":"success",
                    "message":"Access token generated successfully",
                    "data":request.data,
                    "token":headers
                }
            )
        else:
            return Response({
                "message":"Invalid Credentials",
                "data":request.data
            },status=status.HTTP_401_UNAUTHORIZED
            )
    else:
        return Response({
            "message":"Invalid request method",
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)


