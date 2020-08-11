from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.test_helpers import create_user

from core.test_helpers import PASSWORD

from apps.trips.models import Trip


class HttpTripTest(APITestCase):
    def setUp(self):
        user = create_user()
        response = self.client.post(reverse('log_in'), data={
            'username': user.username,
            'password': PASSWORD
        })
        self.access = response.data['access']

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_address='A', drop_off_address='B'),
            Trip.objects.create(pick_up_address='B', drop_off_address='C'),
        ]
        response = self.client.get(reverse('trip:trip_list'), HTTP_AUTHORIZATION=f'Bearer {self.access}')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected_trips_id = [str(trip.id) for trip in trips]
        actual_trips_id = [trip.get('id') for trip in response.data]

        self.assertEqual(expected_trips_id, actual_trips_id)

    def test_user_can_retrieve_trip_by_id(self):
        trip = Trip.objects.create(pick_up_address='A', drop_off_address='B')
        response = self.client.get(trip.get_absolute_url(), HTTP_AUTHORIZATION=f'Bearer {self.access}')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(str(trip.id), response.data.get('id'))
