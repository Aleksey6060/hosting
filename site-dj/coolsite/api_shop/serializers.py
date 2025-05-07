from rest_framework import serializers
from sabaka.models import Category, Flower, Supplier, Delivery, Review, Promotion, Shop, Employee, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class FlowerSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Для отображения категории
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Flower
        fields = ['name', 'description', 'price', 'photo', 'created_at', 'is_available', 'category', 'category_id']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_email', 'phone', 'address']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['name', 'cost', 'estimated_time']

class ReviewSerializer(serializers.ModelSerializer):
    flower = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['flower', 'customer_name', 'rating', 'comment', 'created_at']

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'discount', 'start_date', 'end_date', 'banner']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'phone', 'email', 'working_hours']

class EmployeeSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ['name', 'position', 'shop']

class OrderItemSerializer(serializers.ModelSerializer):
    flower = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = ['flower', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['user', 'created_at', 'delivery_method', 'address', 'total_price', 'status', 'items']