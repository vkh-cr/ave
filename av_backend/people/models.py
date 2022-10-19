from django.db import models as m

from core.models import BaseModel


class Person(BaseModel):
    code = m.CharField(max_length=3, blank=True)
    name = m.CharField(max_length=256)
    e_mail = m.EmailField(max_length=128, blank=True)
    phone = m.CharField(max_length=128, blank=True)
    city = m.CharField(max_length=128, blank=True)

    sections = m.ManyToManyField(through="team.TeamMembership", to="team.TeamSection")

    class Meta:
        constraints = [
            m.UniqueConstraint("code", name="uniq_person_code"),
        ]

    def __str__(self):
        if self.code:
            return f"[{self.code}] {self.name}"
        return f"{self.name}"
