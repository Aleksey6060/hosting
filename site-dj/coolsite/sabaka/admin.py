from django.contrib import admin
from .models import Category, Flower, Supplier, Delivery, Review, Promotion, Shop, Employee, Order, OrderItem

# Inline для отображения позиций заказа внутри заказа
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('price',)
    fields = ('flower', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'delivery_method', 'address', 'total_price', 'created_at']
    list_filter = ['delivery_method', 'created_at']
    search_fields = ['user__username', 'address']
    inlines = [OrderItemInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'category']
    list_filter = ['category', 'is_available']
    search_fields = ['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_email', 'phone']
    search_fields = ['name', 'contact_email']

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'estimated_time']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['flower', 'customer_name', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['customer_name']

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount', 'start_date', 'end_date']
    search_fields = ['title']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'shop']
    search_fields = ['name']