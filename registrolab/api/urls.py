from rest_framework.routers import DefaultRouter
from .views import (
    RegistroLabViewSet,
    AsignaturaViewSet,
    DocenteViewSet,
    LaboratorioViewSet,
    CarreraViewSet
)

router = DefaultRouter()

router.register(r'registros', RegistroLabViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'docentes', DocenteViewSet)
router.register(r'laboratorios', LaboratorioViewSet)
router.register(r'carreras', CarreraViewSet)

urlpatterns = router.urls
