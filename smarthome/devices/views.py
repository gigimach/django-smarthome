from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Local, Ambiente, Dispositivo
from .serializers import LocalSerializer, AmbienteSerializer, DispositivoSerializer

class LocalViewSet(viewsets.ModelViewSet):
  queryset = Local.objects.all()
  serializer_class = LocalSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
  queryset = Ambiente.objects.all()
  serializer_class = AmbienteSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
  queryset = Dispositivo.objects.all()
  serializer_class = DispositivoSerializer

  @action(detail=True, methods=['post'])
  def ligar_desligar(self, request, pk=None):
    dispositivo = self.get_object()
    dispositivo.ligado = not dispositivo.ligado
    dispositivo.save()
    return Response({'ligado': dispositivo.ligado})

  @action(detail=False, methods=['post'])
  def desligar_ambiente(self, request):
    ambiente_id = request.data.get('ambiente_id')
    Dispositivo.objects.filter(ambiente_id=ambiente_id).update(ligado=False)
    return Response({'message': 'Todos os dispositivos do ambiente foram desligados.'})

  @action(detail=False, methods=['post'])
  def desligar_local(self, request):
    local_id = request.data.get('local_id')
    Dispositivo.objects.filter(ambiente__local_id=local_id).update(ligado=False)
    return Response({'message': 'Todos os dispositivos do local foram desligados.'})
