import django_filters
from .models import Server

class ServerFilter(django_filters.FilterSet):
    hostname = django_filters.CharFilter(field_name="hostname", lookup_expr='icontains')

    class Meta:
        model = Server
        fields = ['hostname']