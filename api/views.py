from django.shortcuts import render
from rest_framework import viewsets
from reciclagem.models import Unidade, Curso, Turma, Aluno, TipoResiduos, Reciclagem
from .serializers import *
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from accounts.models import User
from drf_yasg.utils import swagger_auto_schema


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post', 'get']

    @swagger_auto_schema(
        operation_summary="Login do usuário",
        request_body=LoginSerializer
    )

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({
                'message': 'Email e senha são obrigatórios.'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                'message': 'Usuário com esse email não encontrado.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({
                'message': 'Usuário inativo.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({
                'message': 'Senha incorreta.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        last_login = user.last_login
        
        refresh = RefreshToken.for_user(user)
        
        user.last_login = timezone.now()
        user.save()

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': user.id,
            'username': user.username,
            'last_login': last_login,
        }, status=status.HTTP_200_OK)

class UserTokenRefreshView(TokenRefreshView):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [permissions.IsAuthenticated]

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [permissions.IsAuthenticated]

class TipoResiduosViewSet(viewsets.ModelViewSet):
    queryset = TipoResiduos.objects.all()
    serializer_class = TipoResiduosSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReciclagemViewSet(viewsets.ModelViewSet):
    queryset = Reciclagem.objects.all()
    serializer_class = ReciclagemSerializer
    permission_classes = [permissions.IsAuthenticated]
