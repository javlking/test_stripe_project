from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings

import stripe

from .models import Item


def get_item_by_id(request, pk):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        current_item = Item.objects.get(id=pk)

    except Item.DoesNotExist:
        return HttpResponse('Товар не найден')

    get_product_id_stripe = stripe.checkout.Session.create(
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': current_item.name,
            },
            'unit_amount': int(current_item.price),
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/',
        cancel_url='http://localhost:8000/',
      )

    return JsonResponse(get_product_id_stripe)


def get_item(request, pk):
    try:
        current_item = Item.objects.get(id=pk)

    except Exception as e:
        print(e)
        return HttpResponse(status=404)

    return render(request, 'item.html', {'item': current_item})
