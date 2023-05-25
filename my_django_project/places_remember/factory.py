import factory
from django.contrib.auth.models import User
from places_remember.models import Memory
from factory.faker import faker


class MemoryFactory(factory.django.DjangoModuleFactory):
    class Meta:
        model = Memory

    author = User.objects.get_or_create(username='admin')[0]
    title = factory.Faker('Моё воспоминание')
    comment = factory.Faker('Утром мне было весело!')
