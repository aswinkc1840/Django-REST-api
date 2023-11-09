from rest_framework import routers
from .views import MovieViewSet, TheaterViewSet, TicketViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'theaters', TheaterViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = router.urls
