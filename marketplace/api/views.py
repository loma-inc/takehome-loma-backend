from rest_framework import viewsets
from api.models import Marketplace
from api.serializers import MarketplaceSerializer

# Create your views here.


class MarketplaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for the Marketplace model.
    """
    queryset = Marketplace.objects.all().order_by('name')
    serializer_class = MarketplaceSerializer
