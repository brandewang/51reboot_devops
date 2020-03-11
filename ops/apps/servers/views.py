from rest_framework import viewsets, mixins
from .models import Server, NetworkDevice, IP
from .serializers import ServerAutoReportSerializer, NetworkDeviceSerializer, IPSerializer, ServerSerializer
from .filters import ServerFilter

class ServerAutoReportViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
        创建服务器记录
    list:
        返回服务器列表
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer

class ServerViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定服务器信息
    list:
        返回服务器列表
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_class = ServerFilter
    filter_fields = ("hostname",)
    extra_perm_map = {
        "GET": ['servers.view_server']
    }

class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定网卡信息
    list:
        返回网卡列表
    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定IP信息
    list:
        返回IP列表
    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer
