from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .utils import Cart
from django.contrib.auth.mixins import UserPassesTestMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

@login_required(login_url='/login/')
def all_products(request):
    flowers = Flower.objects.filter(is_available=True)
    return render(request, 'all_products.html', {'flowers': flowers})

@login_required(login_url='/login/')
def flowers_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    flowers = Flower.objects.filter(category=category, is_available=True)
    return render(request, 'flowers_by_category.html', {'category': category, 'flowers': flowers})

# Cart functionality
@login_required(login_url='/login/')
def cart_add(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            flower=flower,
            quantity=cd['quantity'],
            reload=cd['reload']
        )
    return redirect('cart_detail')

@login_required(login_url='/login/')
def cart_remove(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.remove(flower)
    return redirect('cart_detail')

@login_required(login_url='/login/')
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['total'] = item['quantity'] * item['price']
    return render(request, 'cart_detail.html', {'cart': cart})

@login_required(login_url='/login/')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    flower=item['flower'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'cart': cart, 'form': form})

@login_required(login_url='/login/')
def order_success(request):
    return render(request, 'order_success.html')

# Authentication views
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

# Order List View for Admin
class OrderListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Order
    template_name = 'orders_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return Order.objects.all().order_by('-created_at')

# Category CRUD
class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories_detail.html'
    context_object_name = 'category'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('category_list')

class FlowerListView(LoginRequiredMixin, ListView):  # Добавлен LoginRequiredMixin
    login_url = '/login/'
    model = Flower
    template_name = 'flowers_list.html'
    context_object_name = 'flowers'
    paginate_by = 10

class FlowerDetailView(LoginRequiredMixin, DetailView):  # Добавлен LoginRequiredMixin
    login_url = '/login/'
    model = Flower
    template_name = 'flowers_detail.html'
    context_object_name = 'flower'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        return context

class FlowerCreateView(LoginRequiredMixin, CreateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'flowers_form.html'
    success_url = reverse_lazy('flower_list')

class FlowerUpdateView(LoginRequiredMixin, UpdateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'flowers_form.html'
    success_url = reverse_lazy('flower_list')

class FlowerDeleteView(LoginRequiredMixin, DeleteView):
    model = Flower
    template_name = 'flowers_delete.html'
    success_url = reverse_lazy('flower_list')

class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('supplier_list')

class DeliveryListView(ListView):
    model = Delivery
    template_name = 'deliveries_list.html'
    context_object_name = 'deliveries'
    paginate_by = 10

class DeliveryDetailView(DetailView):
    model = Delivery
    template_name = 'deliveries_detail.html'
    context_object_name = 'delivery'

class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'deliveries_form.html'
    success_url = reverse_lazy('delivery_list')

class DeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'deliveries_form.html'
    success_url = reverse_lazy('delivery_list')

class DeliveryDeleteView(LoginRequiredMixin, DeleteView):
    model = Delivery
    template_name = 'deliveries_delete.html'
    success_url = reverse_lazy('delivery_list')

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews_delete.html'
    success_url = reverse_lazy('review_list')

class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotions_list.html'
    context_object_name = 'promotions'
    paginate_by = 10

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotions_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(LoginRequiredMixin, CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotions_form.html'
    success_url = reverse_lazy('promotion_list')

class PromotionUpdateView(LoginRequiredMixin, UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotions_form.html'
    success_url = reverse_lazy('promotion_list')

class PromotionDeleteView(LoginRequiredMixin, DeleteView):
    model = Promotion
    template_name = 'promotions_delete.html'
    success_url = reverse_lazy('promotion_list')

class ShopListView(ListView):
    model = Shop
    template_name = 'shops_list.html'
    context_object_name = 'shops'
    paginate_by = 10

class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shops_detail.html'
    context_object_name = 'shop'

class ShopCreateView(LoginRequiredMixin, CreateView):
    model = Shop
    template_name = 'shops_form.html'
    fields = ['name', 'address', 'phone', 'email', 'working_hours']
    success_url = reverse_lazy('shop_list')

class ShopUpdateView(LoginRequiredMixin, UpdateView):
    model = Shop
    template_name = 'shops_form.html'
    fields = ['name', 'address', 'phone', 'email', 'working_hours']
    success_url = reverse_lazy('shop_list')

class ShopDeleteView(LoginRequiredMixin, DeleteView):
    model = Shop
    template_name = 'shops_delete.html'
    success_url = reverse_lazy('shop_list')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees_list.html'
    context_object_name = 'employees'
    paginate_by = 10

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'employees_form.html'
    fields = ['name', 'position', 'shop']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'employees_form.html'
    fields = ['name', 'position', 'shop']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employees_delete.html'
    success_url = reverse_lazy('employee_list')