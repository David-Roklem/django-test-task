import pytest

# from django.contrib.auth.models import User
from places_remember.models import Memory, Coordinates, Userpic, CustomUser


@pytest.mark.django_db
class TestModels:

    def test_user_str(self):
        user = CustomUser.objects.create_user(username='Davvar')
        assert user.__str__() == 'Davvar'

    def test_set_check_password(self):
        user = CustomUser.objects.create_user(username='test_user')
        user.set_password('12345')
        assert user.check_password('12345') is True

    def test_memory_str(self):
        memory = Memory(title='My First Memory')
        assert memory.__str__() == 'My First Memory'

    def test_coordinates_instance(self):
        memory = Memory(title='My First Memory')
        coordinates = Coordinates(
            lat=37.7749, lng=-122.4194, memory=memory
        )
        assert isinstance(coordinates, Coordinates)

    def test_userpic_fields(self):
        userpic = Userpic(
            username='Davvar', pic='http://example.com/image.jpg'
        )
        assert userpic.username == 'Davvar'
        assert userpic.pic == 'http://example.com/image.jpg'
