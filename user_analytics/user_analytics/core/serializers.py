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
    class Meta:
        model = Study
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret
