import django_filters
from .models import (
    Study,
)

class StudyFilter(django_filters.FilterSet):
    id = django_filters.CharFilter()
    sla = django_filters.NumberFilter()
    sla__gt = django_filters.NumberFilter(
        field_name="sla", lookup_expr="gt"
    )
    sla__lt = django_filters.NumberFilter(
        field_name="sla", lookup_expr="lt"
    )
    sla__gte = django_filters.NumberFilter(
        field_name="sla", lookup_expr="gte"
    )
    sla__lte = django_filters.NumberFilter(
        field_name="sla", lookup_expr="lte"
    )

    date = django_filters.DateFilter()
    date__gt = django_filters.DateFilter(
        field_name="date", lookup_expr="gt"
    )
    date__lt = django_filters.DateFilter(
        field_name="date", lookup_expr="lt"
    )
    date__gte = django_filters.DateFilter(
        field_name="date", lookup_expr="gte"
    )
    date__lte = django_filters.DateFilter(
        field_name="date", lookup_expr="lte"
    )


    ordering = django_filters.OrderingFilter(
        fields=(
            ("date", "date"),
            ("modality", "modality"),
            ("body_part", "body_part"),
            ("id", "id"),
            ("sla", "sla"),
            ("assigned_to", "assigned_to"),
        ),
    )

    class Meta:
        model = Study
        fields = {
            "id": ["exact"],
            "body_part": ["exact"],
            "modality": ["exact"],
            "assigned_to": ["exact"],
        }

