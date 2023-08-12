from django.db import models
from django.contrib.auth.models import AbstractUser,  Group, Permission
class CustomUserRegistration(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
        

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set'  # Use a unique related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set'  # Use a unique related_name
    ) 
    def __str__(self) -> str:
        return self.username

    
class keyValue(models.Model):
    user = models.ForeignKey(CustomUserRegistration, on_delete=models.CASCADE)
    key = models.CharField(unique=True,max_length=10)
    value = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.key


