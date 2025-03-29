from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

from core.models import CATEGORY_CHOICES
from .models import Cart, CartItem, Product, Order, OrderItem
from django.utils.translation import gettext_lazy as _


# Create your views here.


class AddProducttoCartView(LoginRequiredMixin, View):
    login_url = reverse_lazy('core:login')
    def post(self, request, pk):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=pk)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1


        cart_item.save()
        return JsonResponse({'success': True})


class ViewCartView(LoginRequiredMixin, ListView):
    model = CartItem
    context_object_name = 'cart'
    paginate_by = 100
    template_name = 'cart.html'
    login_url = reverse_lazy('core:login')

    def get_queryset(self):
        # filtered_cart = Cart.objects.filter(user=self.request.user)
        #return CartItem.objects.filter(cart__in=filtered_cart)
        filtered_cart = Cart.objects.get(user=self.request.user)
        return CartItem.objects.filter(cart=filtered_cart)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context




### context processor

class ConfirmOrderView(LoginRequiredMixin, View):
    login_url = reverse_lazy('core:login')
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        order = Order.objects.create(user=request.user)


        for cart_item in cart_items:
            product = cart_item.product

            if product.not_in_stock():
                messages.error(self.request, _(f'Product not in stock: {product.name}'))
                cart_item.delete()
                return redirect('view_cart')

            product.quantity -= cart_item.quantity
            OrderItem.objects.create(order=order, product=product, quantity=cart_item.quantity)
            product.save()
            cart_item.delete()

        return redirect('orders')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    template_name = 'order_list.html'
    login_url = reverse_lazy('core:login')

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'order_details.html'
    login_url = reverse_lazy('core:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        context['order_items'] = OrderItem.objects.filter(order=self.object)
        return context