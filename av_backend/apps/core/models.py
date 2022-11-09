import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import UUIDField
from model_utils.models import TimeStampedModel, UUIDModel


class User(AbstractUser):
    ...


class BaseModel(TimeStampedModel):
    uuid = UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
