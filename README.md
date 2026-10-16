2)
Ao tentar deletar um local com evento relacionado o django impediu, citando que seria necessário antes deletar os eventos associados. Isso se deu pelo "on_delete" configurado: PROTECT. Ele faz com que ao ao tentar deletar um objeto pai de algum outro não haja êxito na ação. O filho é protegito.

3)
    1-
>>> from django.utils import timezone
>>> e = Evento.objects.filter(inicio__gt=timezone.now())
>>> e
<QuerySet [<Evento: Mecanismo de monitoramento de plantação>, <Evento: Yoga para elevar>, <Evento: INPOR>, <Evento: Etal>]>

    2-
>>> e = Evento.objects.filter(titulo__icontains="python")
>>> e
<QuerySet []>

    3-
>>> e = Evento.objects.filter(inicio__month=timezone.now().month)
>>> e
<QuerySet [<Evento: Oficinas de apoio a alunos de escola pública>, <Evento: Mecanismo de monitoramento de plantação>, <Evento: Yoga para elevar>]>

    4-
>>> e = Evento.objects.filter(categorias__nome__icontains="Tecnologia")
>>> e
<QuerySet [<Evento: Mecanismo de monitoramento de plantação>, <Evento: INPOR>, <Evento: Etal>]>

    5-
>>> e = Evento.objects.exclude(local__nome="Auditório")                
>>> e
<QuerySet [<Evento: ALORN>, <Evento: Mecanismo de monitoramento de plantação>, <Evento: Yoga para elevar>]>

    6-
>>> from django.db.models import Q 
>>> e = Evento.objects.filter(Q(categorias__nome="Tecnologia") | Q(categorias__nome="Extensão"))
>>> e
<QuerySet [<Evento: Mecanismo de monitoramento de plantação>, <Evento: INPOR>, <Evento: Etal>]>

    7-
>>> l = Local.objects.get(nome="Ginásio").eventos.all()
>>> l
<QuerySet [<Evento: ALORN>, <Evento: Yoga para elevar>]>

    8-
>>> i = Evento.objects.get(pk=1).inscricoes.all() 
>>> i
<QuerySet [<Inscricao: Geraldo>, <Inscricao: Guilherme>, <Inscricao: Victória>]>

>>> i = Evento.objects.get(pk=1).inscricoes.all().count()
>>> i
3

    9-
>>> l = Local.objects.filter(eventos__atividades__palestrante__icontains="Silva")
>>> l
<QuerySet []>

    10-
>>> r = Evento.objects.get(pk=2).relatorio 
Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "C:\Users\rodri\Documents\ADS\Irlarn\RevisãoProva1-DSW\Revis-o-Prova1-DSW\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 534, in __get__
    raise self.RelatedObjectDoesNotExist(
eventos.models.Evento.relatorio.RelatedObjectDoesNotExist: Evento has no relatorio.

>>> Relatorio.objects.create(presentes=13, evento=Evento.objects.get(pk=2))
<Relatorio: 13>

>>> r = Evento.objects.get(pk=2).relatorio
>>> r                                     
<Relatorio: 13>

    Um querySet preguiçoso é aquele que só efetua a ocnsulta no banco quando é chamado, implicando que o mesmo querySet pode pegar valores diferentes em chamdas distintas se houver uma alteração no banco entre as chamadas.