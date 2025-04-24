from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils.text import slugify

# Signal para criar dados padrão automaticamente
'''
@receiver(post_migrate)
def create_default_residuos_and_unidades(sender, **kwargs):
    if sender.label == 'reciclagem':  # Substitua 'app_name' pelo nome da sua app
        # Criando os tipos de resíduos padrão
        TipoResiduo.objects.get_or_create(codigo='aluminio', nome='Alumínio')
        TipoResiduo.objects.get_or_create(codigo='vidro', nome='Vidro')
        TipoResiduo.objects.get_or_create(codigo='pano', nome='Pano')
        TipoResiduo.objects.get_or_create(codigo='pet', nome='PET')
        TipoResiduo.objects.get_or_create(codigo='organico', nome='Orgânico')
        TipoResiduo.objects.get_or_create(codigo='papeis_papelao', nome='Papéis e Papelões')
        TipoResiduo.objects.get_or_create(codigo='madeira', nome='Madeira')
        TipoResiduo.objects.get_or_create(codigo='pilhas_baterias', nome='Pilhas e Baterias')
        TipoResiduo.objects.get_or_create(codigo='lixo_hospitalar', nome='Lixo Hospitalar')
        TipoResiduo.objects.get_or_create(codigo='residuos_solidos', nome='Resíduos Sólidos não descartados')
        
        # Criando as unidades padrão
        Unidade.objects.get_or_create(code='alcindo_cancela', nome='Unama Alcindo Cancela')
        Unidade.objects.get_or_create(code='ananindeua', nome='Unama Ananindeua')
        Unidade.objects.get_or_create(code='outro', nome='Outro')

        # Criando os turnos padrão
        Turno.objects.get_or_create(code='matutino', nome='Matutino')
        Turno.objects.get_or_create(code='vespertino', nome='Vespertino')
        Turno.objects.get_or_create(code='noturno', nome='Noturno')
'''

# Models ajustados para não alterar o comportamento atual

class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Unidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='unidades', blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='unidades', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cidade.nome} - {self.estado.nome})"

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'

class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    duracao = models.IntegerField(help_text="Duração em Semestres")
    coordenador = models.CharField(max_length=100, help_text="Nome do Coordenador")
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return f"{self.nome} ({self.unidade.nome})"

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class Turma(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    semestre = models.IntegerField()
    turno = models.CharField(max_length=50, choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

class TipoResiduos(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = 'Tipo de Resíduo'
        verbose_name_plural = 'Tipos de Resíduos'

class Reciclagem(models.Model):
    quantidade = models.FloatField(help_text="Quantidade em kg")
    tipo_residuo = models.ForeignKey(TipoResiduos, on_delete=models.CASCADE, related_name='reciclagens')
    aluno = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='reciclagens', blank=True, null=True)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.data} - {self.tipo_residuo.nome} ({self.unidade.nome})"

    class Meta:
        verbose_name = 'Reciclagem'
        verbose_name_plural = 'Reciclagens'