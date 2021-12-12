from rest_framework import routers
from app.views import ContactViewSet
router = routers.SimpleRouter()

router.register(r'', ContactViewSet)