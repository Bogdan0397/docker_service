

from django.conf import settings
from django.core.cache import cache
from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework import filters

from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):

    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client',
        queryset =Client.objects.all().select_related('user').only('company_name',
                                                                   'user__email')))


    serializer_class = SubscriptionSerializer


    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response_data = {'result':response.data}

        price_cache = cache.get(settings.PRICE_CACHE_NAME)

        if price_cache:
            total_price = price_cache
        else:
            total_price = self.queryset.aggregate(total=Sum('price')).get('total')
            cache.set(settings.PRICE_CACHE_NAME,total_price,60*60)

        response_data['total_amount'] = self.queryset.aggregate(total=Sum('price')).get('total')
        response.data = response_data

        return response
