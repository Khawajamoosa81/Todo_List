
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapi import views

router = routers.DefaultRouter()
router.register('breed', views.BreedView)
router.register('dog', views.DogView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
