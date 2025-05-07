from .models import Flower

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, flower, quantity=1, reload=False):
        flower_id = str(flower.id)
        if flower_id not in self.cart:
            self.cart[flower_id] = {'quantity': 0, 'price': float(flower.price)}
        if reload:
            self.cart[flower_id]['quantity'] = quantity
        else:
            self.cart[flower_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, flower):
        flower_id = str(flower.id)
        if flower_id in self.cart:
            del self.cart[flower_id]
            self.save()

    def __iter__(self):
        flower_ids = self.cart.keys()
        flowers = Flower.objects.filter(id__in=flower_ids)
        for flower in flowers:
            self.cart[str(flower.id)]['flower'] = flower
            yield self.cart[str(flower.id)]

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True