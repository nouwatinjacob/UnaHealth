import factory
import uuid
from django.contrib.auth import get_user_model
from readings.models import Reading

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    username = 'test1@yahoo.com'
    user_id = uuid.uuid4()
    password = factory.PostGenerationMethodCall('set_password', 'olukayss')

    is_superuser = True
    is_staff = True
    is_active = True
    
    
class ReadingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reading
        
    user = factory.SubFactory(UserFactory)
    device = "FreeStyle LibreLink"
    serial_number = "e09bb0f0-018b-429b-94c7-62bb306a0564"
    device_timestamp = "2022-02-08T09:08:00Z"
    recording_type = "0"
    glucose_value_history = "138"