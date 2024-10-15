from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ProductViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
