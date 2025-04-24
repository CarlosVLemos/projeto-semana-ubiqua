from django.db import models

class TipoResiduo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=50, unique=True)

    # tipos de residus
    TIPO_ALUMINIO = 'aluminio'
    TIPO_VIDRO = 'vidro'
    TIPO_PANO = 'pano'
    TIPO_PET = 'pet'
    TIPO_ORGANICO = 'organico'
    TIPO_PAPEIS_PAPELAO = 'papeis_papelão'
    TIPO_MADEIRA = 'madeira'
    TIPO_PILHAS_BATERIAS = 'pilhas_baterias'
    TIPO_LIXO_HOSPITALAR = 'lixo_hospitalar'
    TIPO_RESIDUOS_SOLIDOS = 'residuos_solidos'

    TIPOS_RESIDUOS = [
        (TIPO_ALUMINIO, 'Alumínio'),
        (TIPO_VIDRO, 'Vidro'),
        (TIPO_PANO, 'Pano'),
        (TIPO_PET, 'PET'),
        (TIPO_ORGANICO, 'Orgânico'),
        (TIPO_PAPEIS_PAPELAO, 'Papéis e Papelões'),
        (TIPO_MADEIRA, 'Madeira'),
        (TIPO_PILHAS_BATERIAS, 'Pilhas e Baterias'),
        (TIPO_LIXO_HOSPITALAR, 'Lixo Hospitalar'),
        (TIPO_RESIDUOS_SOLIDOS, 'Resíduos Sólidos não descartados'),
    ]

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Resíduo'
        verbose_name_plural = 'Tipos de Resíduos'

class Reciclagem(models.Model):
    TURNO_CHOICES = [
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno'),
    ]
    UNIDADE_CHOICES = [
        ('alcindo_cancela', 'Unama Alcindo Cancela'),
        ('ananindeua',     'Unama Ananindeua'),
        ('outro',          'Outro'),
    ]
    # TIPO_RESIDUO_CHOICES = [
    #     ('papel',    'Papel'),
    #     ('organico', 'Orgânico'),
    #     ('pet',      'PET'),
    #     ('metal',    'Metal'),
    #     ('aluminio', 'Alumínio'),
    #     ('vidro',    'Vidro'),
    #     ('outro',    'Outro'),
    # ]

    nome          = models.CharField(max_length=100)
    matricula     = models.CharField(max_length=20)
    turma         = models.CharField(max_length=20)
    turno         = models.CharField(max_length=20, choices=TURNO_CHOICES)
    semestre      = models.CharField(max_length=10)
    unidade       = models.CharField(max_length=50, choices=UNIDADE_CHOICES)
    
    # TipoResiduo
    tipo_residuo= models.ForeignKey(TipoResiduo, on_delete=models.PROTECT, verbose_name='Tipo de Residuo')


    quantidade    = models.PositiveIntegerField()
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} – {self.tipo_residuo} ({self.quantidade})"
    

