# actividades/api/urls.py
from rest_framework.routers import DefaultRouter
from actividades.api.views import TipoActividadViewSet, ActividadViewSet  # Ajusta la ruta


router = DefaultRouter()
router.register('tipos-actividad', TipoActividadViewSet, basename='tipos-actividad')
router.register('actividades', ActividadViewSet, basename='actividades')
urlpatterns = router.urls
