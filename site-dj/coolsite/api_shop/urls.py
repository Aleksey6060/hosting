from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, FlowerViewSet, SupplierViewSet, DeliveryViewSet,
    ReviewViewSet, PromotionViewSet, ShopViewSet, EmployeeViewSet, OrderViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'flowers', FlowerViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]