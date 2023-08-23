from django.urls import path

from orders.views import OrderCreateView, CanceledTemplateView,   SuccessTemplateView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order-canceled'),
    path('order-success/', SuccessTemplateView.as_view(), name='order-success'),
    path('', OrderListView.as_view(), name='orders_list'),
]
