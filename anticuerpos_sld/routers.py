from rest_framework import routers
from anticuerpos_sld_app.viewsets import PacienteViewSet


router = routers.DefaultRouter()


router.register(r'pacientes', PacienteViewSet)