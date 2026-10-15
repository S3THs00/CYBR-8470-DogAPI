from django.contrib import admin
from django.urls import path
from dogapi.controllers import (
    DogList,
    DogDetail,
    BreedList,
    BreedDetail,
)


# URL patterns for the class-based API implementation.
# List endpoints handle GET and POST.
# Detail endpoints handle GET, PUT, and DELETE.
urlpatterns = [
    path('admin/', admin.site.urls),

    # Dog API endpoints
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),

    # Breed API endpoints
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]