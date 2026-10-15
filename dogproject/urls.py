from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dogapi.views import DogViewSet, BreedViewSet


# Router automatically creates the REST API URL patterns
# for both Dog and Breed endpoints.
router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Adds the Dog and Breed API endpoints under /api/
    path('api/', include(router.urls)),
]