from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('how-to-find/', views.how_to_find, name='how_to_find'),
    path('categories/', views.categories, name='categories'),
    path('all-products/', views.all_products, name='all_products'),
    # Cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:flower_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:flower_id>/', views.cart_remove, name='cart_remove'),
    path('order/create/', views.order_create, name='order_create'),
    path('order-success/', views.order_success, name='order_success'),
    # Authentication URLs
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    # Flower URLs
    path('flowers/', FlowerListView.as_view(), name='flower_list'),
    path('flowers/<int:pk>/', FlowerDetailView.as_view(), name='flower_detail'),
    path('flowers/create/', FlowerCreateView.as_view(), name='flower_create'),
    path('flowers/<int:pk>/update/', FlowerUpdateView.as_view(), name='flower_update'),
    path('flowers/<int:pk>/delete/', FlowerDeleteView.as_view(), name='flower_delete'),
    # Flowers by Category
    path('flowers/category/<int:category_id>/', views.flowers_by_category, name='flowers_by_category'),
    # Category URLs
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    # Supplier URLs
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
    # Delivery URLs
    path('deliveries/', DeliveryListView.as_view(), name='delivery_list'),
    path('deliveries/<int:pk>/', DeliveryDetailView.as_view(), name='delivery_detail'),
    path('deliveries/create/', DeliveryCreateView.as_view(), name='delivery_create'),
    path('deliveries/<int:pk>/update/', DeliveryUpdateView.as_view(), name='delivery_update'),
    path('deliveries/<int:pk>/delete/', DeliveryDeleteView.as_view(), name='delivery_delete'),
    # Review URLs
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    # Promotion URLs
    path('promotions/', PromotionListView.as_view(), name='promotion_list'),
    path('promotions/<int:pk>/', PromotionDetailView.as_view(), name='promotion_detail'),
    path('promotions/create/', PromotionCreateView.as_view(), name='promotion_create'),
    path('promotions/<int:pk>/update/', PromotionUpdateView.as_view(), name='promotion_update'),
    path('promotions/<int:pk>/delete/', PromotionDeleteView.as_view(), name='promotion_delete'),
    # Shop URLs
    path('shops/', views.ShopListView.as_view(), name='shop_list'),
    path('shops/<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
    path('shops/create/', views.ShopCreateView.as_view(), name='shop_create'),
    path('shops/<int:pk>/update/', views.ShopUpdateView.as_view(), name='shop_update'),
    path('shops/<int:pk>/delete/', views.ShopDeleteView.as_view(), name='shop_delete'),
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    # Order URLs for Admin
    path('orders/', views.OrderListView.as_view(), name='order_list'),
]