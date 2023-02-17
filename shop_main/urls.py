from django.urls import path
from .views import get_item_by_id, get_item

urlpatterns = [
    path('buy/<int:pk>', get_item_by_id),
    path('item/<int:pk>', get_item)
]
