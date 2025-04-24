from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils.text import slugify

# Signal para criar dados padrão automaticamente
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


# Models ajustados para não alterar o comportamento atual

class TipoResiduo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Resíduo'
        verbose_name_plural = 'Tipos de Resíduos'


class Unidade(models.Model):
    ALCINDO_CANCELA = 'alcindo_cancela'
    ANANINDEUA = 'ananindeua'
    OUTRO = 'outro'
    UNIDADES = [
        (ALCINDO_CANCELA, 'Unama Alcindo Cancela'),
        (ANANINDEUA, 'Unama Ananindeua'),
        (OUTRO, 'Outro'),
    ]

    code = models.CharField(
        max_length=50,
        choices=UNIDADES,
        unique=True,
        help_text='Código interno da unidade',
        default=ALCINDO_CANCELA  # Definindo um valor padrão
    )
    nome = models.CharField(
        max_length=100,
        help_text='Nome completo da unidade'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'


class Turno(models.Model):
    MATUTINO   = 'matutino'
    VESPERTINO = 'vespertino'
    NOTURNO    = 'noturno'
    TURNOS = [
        (MATUTINO,   'Matutino'),
        (VESPERTINO, 'Vespertino'),
        (NOTURNO,    'Noturno'),
    ]

    code = models.CharField(
        max_length=20,
        choices=TURNOS,
        unique=True,
        help_text='Código interno do turno'
    )
    nome = models.CharField(
        max_length=20,
        help_text='Descrição amigável do turno'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'


class Reciclagem(models.Model):
    nome           = models.CharField(max_length=100)
    matricula      = models.CharField(max_length=20)
    turma          = models.CharField(max_length=20)
    turno          = models.ForeignKey(
                        Turno,
                        on_delete=models.PROTECT,
                        verbose_name='Turno'
                     )
    semestre       = models.CharField(max_length=10)
    unidade        = models.ForeignKey(
                        Unidade,
                        on_delete=models.PROTECT,
                        verbose_name='Unidade'
                     )
    tipo_residuo   = models.ForeignKey(
                        TipoResiduo,
                        on_delete=models.PROTECT,
                        verbose_name='Tipo de Resíduo'
                     )
    quantidade     = models.PositiveIntegerField()
    criado_em      = models.DateTimeField(auto_now_add=True)
    atualizado_em  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} – {self.tipo_residuo} ({self.quantidade})"
