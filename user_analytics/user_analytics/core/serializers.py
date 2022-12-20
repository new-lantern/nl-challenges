from collections import OrderedDict
from operator import itemgetter

from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers

from .models import (
    User,
    Study,
)

class UserSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field="core.User.id", read_only=True)
    UserName = serializers.CharField(source="name", read_only=True)
    SubspecialtyModality = serializers.CharField(source="subspecialty_modality", read_only=True)
    SubspecialtyBodyPart = serializers.CharField(source="subspecialty_body_part", read_only=True)
    SlaGoal = serializers.FloatField(source="sla_goal", read_only=True)
    RevenueGoal = serializers.IntegerField(source="revenue_goal", read_only=True)
    StudiesGoal = serializers.IntegerField(source="revenue_goal", read_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret

class StudySerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field="core.Study.id", read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field="core.User.id"),
        queryset=User.objects.all(),
        many=True,
    )
    StudyTimestamp = serializers.TimeField(source="timestamp", read_only=True)
    StudyRevenue = serializers.IntegerField(source="revenue", read_only=True)
    StudyModality = serializers.CharField(source="modality", read_only=True)
    StudyBodyPart = serializers.CharField(source="body_part", read_only=True)
    StudySla = serializers.IntegerField(source="sla", read_only=True)

    
    class Meta:
        model = Study
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret
