from rest_framework import serializers
from reciclagem.models import Unidade, Curso, Turma, Aluno, TipoResiduos, Reciclagem
class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TipoResiduosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResiduos
        fields = '__all__'

class ReciclagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciclagem
        fields = '__all__'



