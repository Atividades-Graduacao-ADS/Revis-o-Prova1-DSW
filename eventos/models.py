from django.db import models

# Create your models here.

class Local(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
            return f"{self.nome}"
        
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, related_name='eventos')
    categorias = models.ManyToManyField(Categoria, blank=True, related_name='eventos')
    
    def __str__(self):
            return f"{self.titulo}"
        
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['inicio']
    
    @property
    def vagas_restantes(self):
        return self.local.capacidade - self.inscricoes.count()


class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    palestrante = models.CharField(max_length=100)
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='atividades')
    
    def __str__(self):
            return f"{self.titulo}"
        
    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ['horario']


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    
    def __str__(self):
            return f"{self.nome}"
        
    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"


class Relatorio(models.Model):
    presentes = models.PositiveIntegerField()
    observacoes = models.TextField(null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name='relatorio')
    
    def __str__(self):
        return f"{self.presentes}"
    
    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"