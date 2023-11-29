from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import calculate_vendor_metrics

@api_view(['GET'])
def get_vendor_performance(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    calculate_vendor_metrics(vendor)
    serializer = VendorSerializer(vendor)
    return Response(serializer.data)


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
