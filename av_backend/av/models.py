from django.db import models as m

from core.models import BaseModel


class AVYear(BaseModel):
    """AV year / edition"""

    title = m.CharField(max_length=128)
    start_dt = m.DateTimeField()
    end_dt = m.DateTimeField()

    class Meta:
        ...
