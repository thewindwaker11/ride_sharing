from django.contrib.auth import get_user_model

PASSWORD = 'password'


def create_user(username='user@ride.com', password=PASSWORD):
    return get_user_model().objects.create_user(
        username=username,
        first_name='user_first',
        last_name='user_last',
        password=password
    )
