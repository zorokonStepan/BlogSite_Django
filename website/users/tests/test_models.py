import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john1', '1lennon@thebeatles.com', 'joh1npassword')
    assert User.objects.count() == 1



