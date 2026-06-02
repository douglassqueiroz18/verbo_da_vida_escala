from rest_framework.routers import DefaultRouter
from core.views import PessoaViewSet
from .views import PessoaViewSet, DepartamentoViewSet, EscalaViewSet, EventoViewSet
router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'escalas', EscalaViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = router.urls