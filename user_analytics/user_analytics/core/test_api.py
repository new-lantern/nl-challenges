import json
import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from .factories import (
    StudyFactory,
    UserFactory,
)

pytestmark = pytest.mark.django_db

def test_assigned_to():
    client = APIClient()

    s = StudyFactory()
    user = UserFactory()
    UserFactory()
    res = client.put(
        reverse("api:study-detail", args=(s.id,)), {"assigned_to": [user.id.hashid]}
    )

    assert res.status_code == 200
    assert res.data["assigned_to"] == [user.id.hashid]

def test_filters_by_modality():
    client = APIClient()

    study_a = StudyFactory(modality="CT")
    StudyFactory(modality="MR")
    res = client.get(reverse("api:study-list"), {"modality": "CT"})
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["id"] == study_a.id

def test_filters_by_assigned_to():
    client = APIClient()

    user = UserFactory()
    s = StudyFactory()
    s.assigned_to.set([user.id.hashid])
    StudyFactory()
    res = client.get(reverse("api:study-list"), {"assigned_to": [user.id.hashid]})
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["id"] == s.id

def test_multi_filters():
    client = APIClient()

    user = UserFactory()
    study_a = StudyFactory(modality="CT")
    study_a.assigned_to.set([user.id.hashid])
    StudyFactory(modality="CT")
    study_b = StudyFactory()
    study_b.assigned_to.set([user.id.hashid])
    StudyFactory()
    
    res = client.get(
        reverse("api:study-list"),
        {
            "assigned_to": [user.id.hashid],
            "modality": "CT"
        }
    )
    assert res.status_code == 200
    assert len(res.data) == 1
    assert res.data[0]["id"] == study_a.id
