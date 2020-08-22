import pytest

from everycheese.users.models import User

# Connects our tests with our database
pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"