from rest_framework import serializers
from .models import CustomUserRegistration , keyValue
from django.contrib.auth.hashers import make_password

class CustomUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserRegistration
        fields = ["id", "username", "password", "email", "full_name", "age", "gender"]

    def create(self, validated_data):
        password = make_password(validated_data["password"])
        user = CustomUserRegistration.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password=password,
            full_name=validated_data["full_name"],
            age=validated_data["age"],
            gender=validated_data["gender"]
        )
        return user    

class CustomDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  keyValue
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)

    

    


    
