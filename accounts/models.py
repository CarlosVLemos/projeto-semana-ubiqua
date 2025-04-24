from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    turma = models.ForeignKey('reciclagem.Turma', on_delete=models.CASCADE, related_name='usuarios', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = [
            ('view_own_user', 'Can view own user')
        ]
        