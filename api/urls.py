from django.urls import path
from .views import *

urlpatterns = [
    path('token/', 
         TokenGenerateAPIView.as_view(),
         name='token'
    ),
    path('vendors/', 
         VendorListCreateAPIView.as_view(),
         name='vendors'
    ),
    path('vendors/<int:vendor_id>/', 
         VendorRetrieveUpdateDeleteAPIView.as_view(),
         name='vendors_ids'
    ),
    path('purchase_orders/', 
         PurchaseOrderListCreateAPIView.as_view(),
         name='purchase-orders'
    ),
    path('purchase_orders/<int:po_id>/', 
         PurchaseOrderRetrieveUpdateDeleteAPIView.as_view(),
         name='purchase-orders_ids'
    ),
    path('vendors/<int:vendor_id>/performance/', 
         VendorPerformanceAPIView.as_view(),
         name='vendors_ids-performance'
    ),
    path('purchase_orders/<int:po_id>/acknowledge/', 
         AcknowledgePurchaseOrderAPIView.as_view(),
         name='purchase_orders_ids-acknoledge'
    ),
]
