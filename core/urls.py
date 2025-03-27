from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/<str:category>/', views.ProductCategoryListView.as_view(), name='category_products'),
    path('add/', views.CreateProductView.as_view(), name='add_product'),
    path('products/details/<int:pk>', views.ProductDetailsView.as_view(), name='product_details'),
    path('products/update/<int:pk>', views.UpdateProductView.as_view(), name='update_product'),
]