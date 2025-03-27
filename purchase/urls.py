from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.ViewCartView.as_view(), name='view_cart'),
    path('add_to_cart/<int:pk>', views.AddProducttoCartView.as_view(), name='add_to_cart'),
    path('', views.OrderListView.as_view(), name='orders'),
    path('confirm_order/', views.ConfirmOrderView.as_view(), name='confirm_order'),
    path('details/<int:pk>', views.OrderDetailView.as_view(), name='order_details'),
]
