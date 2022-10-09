from django.contrib.auth.models import AbstractUser
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel, UUIDModel


class User(AbstractUser):
    ...


class BaseModel(TimeStampedModel):
    uuid = UUIDField(
        version=4,
        editable=False,
    )

    class Meta:
        abstract = True
