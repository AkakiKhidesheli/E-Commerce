from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from core.forms import ProductForm, ProductImageFormSet
from core.mixins import AddProductMixin, UpdateProductMixin, DeleteProductMixin
from core.models import Product, ProductImage, CATEGORY_CHOICES


# Create your views here.

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 4
    template_name = 'products/product_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = CATEGORY_CHOICES
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories_with_products = {}
        for category_key, category_name in CATEGORY_CHOICES:
            products_in_category = Product.objects.filter(category=category_key).order_by('-created_at')

            paginator = Paginator(products_in_category, self.paginate_by)
            page_number = self.request.GET.get(f'page_{category_key}', 1)
            page_obj = paginator.get_page(page_number)

            categories_with_products[category_name] = page_obj

        context['categories_with_products'] = categories_with_products
        context['categories'] = CATEGORY_CHOICES
        return context

class ProductCategoryListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    template_name = 'products/product_category_list.html'

    def get_queryset(self):
        category_key = self.kwargs['category']

        valid_categories = dict(CATEGORY_CHOICES).keys()
        if category_key not in valid_categories:
            return Product.objects.none()

        return Product.objects.filter(category=category_key).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_key = self.kwargs['category']
        context['current_category'] = dict(CATEGORY_CHOICES).get(category_key, '')
        context['categories'] = CATEGORY_CHOICES
        return context


class CreateProductView(LoginRequiredMixin, AddProductMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('core:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_formset'] = ProductImageFormSet(queryset=ProductImage.objects.none())
        context['categories'] = CATEGORY_CHOICES
        return context

    def form_valid(self, form):
        product = form.save()

        image_formset = ProductImageFormSet(self.request.POST, files=self.request.FILES)

        for image_form in image_formset:
            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.product = product
                image.save()

        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context


class UpdateProductView(LoginRequiredMixin, UpdateProductMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update_product.html'
    login_url = 'authentication:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

    def get_success_url(self):
        success_url = reverse_lazy('core:product_details', kwargs={'pk': self.object.pk})
        return success_url


class DeleteProductView(LoginRequiredMixin, DeleteProductMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('core:product_list')