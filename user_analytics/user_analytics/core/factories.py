from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from .models import (
    User,
    Study,
)

class UserFactory(DjangoModelFactory):
    name = Faker("name")
    subspecialty_modality = Faker(
        "random_element",
        elements=(
            "CT",
            "MR",
            "XA",
            "CR",
            "DX",
            "PET",
            "NM",
            "US",
            "RF",
            "ECG",
            "SC",
            "MG",
        ),
    )
    subspecialty_body_part = Faker(
        "random_element",
        elements=(
            "ABDOMEN",
            "ANKLE",
            "BACK",
            "BREAST",
            "CHEST",
            "WHOLEBODY",
            "FOOT",
            "HAND",
            "HEAD",
            "HIP",
            "KNEE",
            "LEG",
            "NECK",
            "SHOULDER",
            "SPINE",
            "ARM",
            "UTERUS",
            "WRIST",
        ),
    )
    class Meta:
        model = User

class StudyFactory(DjangoModelFactory):
    timestamp = Faker("time")
    modality = Faker(
        "random_element",
        elements=(
            "CT",
            "MR",
            "XA",
            "CR",
            "DX",
            "PET",
            "NM",
            "US",
            "RF",
            "ECG",
            "SC",
            "MG",
        ),
    )
    body_part = Faker(
        "random_element",
        elements=(
            "ABDOMEN",
            "ANKLE",
            "BACK",
            "BREAST",
            "CHEST",
            "WHOLEBODY",
            "FOOT",
            "HAND",
            "HEAD",
            "HIP",
            "KNEE",
            "LEG",
            "NECK",
            "SHOULDER",
            "SPINE",
            "ARM",
            "UTERUS",
            "WRIST",
        ),
    )

    class Meta:
        model = Study
