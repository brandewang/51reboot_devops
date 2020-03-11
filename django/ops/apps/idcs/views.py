from rest_framework import viewsets
from .models import Idc
from .serializers import IdcSerializer

class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定Idc信息
    list:
        返回Idc列表
    update:
        更新Idc信息
    destroy:
        删除Idc信息
    create:
        创建Idc记录
    partial_update:
        更新部分字段
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

