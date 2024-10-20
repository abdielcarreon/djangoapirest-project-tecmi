from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldsViewSet

router = DefaultRouter()
router.register(r'ProGolWatch', FieldsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]  

# Basic Representation Created Routes  

# GET /ProGolWatch/: Listed of all registers
# POST /ProGolWatch/: Create a new register
# GET /ProGolWatch/{id}: Get details about one specific register
# PUT /Tasks/{id}: Update register
# DELETE /Tasks/{id}: Delete one register