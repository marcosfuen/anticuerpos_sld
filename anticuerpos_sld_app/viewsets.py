from rest_framework import viewsets, filters, status
from .serializers import ResultadoSerializer, TipoTestSerializer, PacienteSerializer
from .models import Resultado, TipoTest, Paciente
from rest_framework.decorators import action
from datetime import datetime
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('-fecha')
    serializer_class = PacienteSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('carIdentidad', 'nombresApellidos', 'tipoTest__nombre', 'resultado__nombre', 'fecha', 'fechaRecibido')
    ordering_fields = ('fecha',)
    http_method_names = ['get', 'head']

    @action(detail=False, methods=['get'])
    def todos_los_Pacientes_anno_actual(self, request):
        """
        Mostrar todos los pacietes del año actual. 
        """
        # Filtrar todos los pacietes del año actual. 
        today = datetime.today()
        self.queryset = self.get_queryset().filter(fecha__year=today.year).order_by('-fecha')

        # Aplicar otros filtros del viewset
        queryset = self.filter_queryset(self.queryset)

        # # Paginar resultados
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # Serializar resultados
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)