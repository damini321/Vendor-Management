from django.urls import path
from .views import VendorListCreateView, VendorDetailView, \
    PurchaseOrderListCreateView, PurchaseOrderDetailView, get_vendor_performance

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('api/vendors/<int:vendor_id>/performance/', get_vendor_performance, name='vendor-performance'),
]
