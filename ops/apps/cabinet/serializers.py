from rest_framework import serializers
from idcs.serializers import IdcSerializer
from .models import Cabinet
from idcs.models import Idc

class CabinetSerializer(serializers.Serializer):
    idc = serializers.PrimaryKeyRelatedField(many=False, queryset=Idc.objects.all())
    name = serializers.CharField(required=True)

    def to_representation(self, instance):
        """
        序列化转为json的最后一步
        """
        idc_obj = instance.idc
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret["idc"] = {
            'id': idc_obj.id,
            'name': idc_obj.name
        }
        return ret

    def to_internal_value(self, data):
        """
        反序列化第一步: 拿到的是提交过来的原始数据: QueryDict => request.GET, request.POST
        """
        print(data)
        return super(CabinetSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        raise serializers.ValidationError("create error")
        return Cabinet.objects.create(**validated_data)