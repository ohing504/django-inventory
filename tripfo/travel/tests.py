import pytest
from django.core.urlresolvers import reverse
from rest_framework import status

from travel.models import Travel


def travel_list_url():
    return reverse('api:travel-list')


def travel_detail_url(**kwargs):
    return reverse('api:travel-detail', **kwargs)


@pytest.fixture
def travel_list():
    data_list = [
        {'title': 'Travel Title 1'},
        {'title': 'Travel Title 2'},
        {'title': 'Travel Title 3'},
    ]
    Travel.objects.bulk_create([Travel(**data) for data in data_list])

    return Travel.objects.all()


@pytest.mark.django_db
def test_retrieve_travel_detail(client, travel_list):
    for travel in travel_list:
        response = client.get(travel_detail_url(kwargs={'pk': travel.id}))

        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == travel.title


@pytest.mark.django_db
def test_retrieve_travel_list(client, travel_list):
    response = client.get(travel_list_url())

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(travel_list)

    for idx in range(len(response.data)):
        assert response.data[idx]['id'] == travel_list[idx].id
        assert response.data[idx]['title'] == travel_list[idx].title


@pytest.mark.django_db
def test_update_travel_without_authentication(client):
    travel = {'title': 'Travel Title'}
    response = client.post(travel_list_url(), json=travel)

    assert response.status_code == status.HTTP_403_FORBIDDEN
