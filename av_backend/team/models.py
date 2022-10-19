from django.db import models as m

from core.models import BaseModel


class TeamSection(BaseModel):
    code = m.CharField(max_length=32)
    name = m.CharField(max_length=256)
    e_mail = m.EmailField(max_length=128, blank=True)
    phone = m.CharField(max_length=128, blank=True)

    members = m.ManyToManyField(through="team.TeamMembership", to="people.Person")

    class Meta:
        constraints = [
            m.UniqueConstraint("code", name="uniq_section_code"),
        ]

    def __str__(self):
        return f"[{self.code}] {self.name}"


class TeamMembership(BaseModel):
    person = m.ForeignKey(
        "people.Person",
        on_delete=m.CASCADE,
        related_name="member_sections",
    )
    section = m.ForeignKey(
        TeamSection,
        on_delete=m.RESTRICT,
        related_name="member_persons",
    )

    class Meta:
        constraints = [
            m.UniqueConstraint("person", "section", name="uniq_team_membership"),
        ]

    def __str__(self):
        return f"{self.person.code}@{self.section.code}"
