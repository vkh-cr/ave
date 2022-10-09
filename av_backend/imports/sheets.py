import re

from apiclient import discovery
from django.db import transaction
from google.oauth2 import service_account

from django.conf import settings

from people.models import Person
from team.models import TeamSection, TeamMembership

SCOPES = [
    # "https://www.googleapis.com/auth/drive",
    # "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]


class TeamImportService:
    SECRET_FILE = settings.GOOGLE_APIS_CREDENTIALS_FILE
    DOCUMENT_ID = settings.AV_TEAM_SHEET_ID

    RANGE = "List 1!C3:I50"
    PEOPLE_FIELDS = (
        "name",
        "code",
        "section",
        "section_email",
        "email",
        "phone",
        "city",
    )
    SECTIONS_RANGE = "List 1!E3:F50"
    SECTIONS_FIELDS = (
        "name",
        "email",
    )

    def parse_multiple_values(self, data, separator=";"):
        return data.split(separator)

    def take_first(self, values, none_value=""):
        return values[0] if values else none_value

    def mk_row_data(self, row, fields):
        return dict(zip(fields, (row + ([None] * (len(fields) - len(row))))))

    def retrieve_sheet_data(self, sheet_id, sheet_range):
        credentials = service_account.Credentials.from_service_account_file(
            self.SECRET_FILE,
            scopes=SCOPES,
        )
        service = discovery.build("sheets", "v4", credentials=credentials)

        sheets = service.spreadsheets()
        result = (
            sheets.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
        )

        return result.get("values", [])

    def parse_section_code(self, section_name):
        code_regex = re.compile(r"\W")

        code = section_name
        code = code_regex.split(code)[0]
        code = code_regex.sub(" ", code).upper()

        return code

    def _sections(self, data, fields=SECTIONS_FIELDS):
        for row in data:
            row_data = self.mk_row_data(row, fields)

            if not row_data.get("email"):
                continue

            row_data["email"] = self.parse_multiple_values(row_data["email"])
            row_data["code"] = self.parse_section_code(row_data["name"])

            yield row_data

    def _persons(self, data, fields=PEOPLE_FIELDS):
        for row in data:
            row_data = self.mk_row_data(row, fields)

            if not row_data.get("code"):
                continue

            row_data.pop("section_email", None)
            row_data["section"] = self.parse_section_code(row_data["section"])
            row_data["email"] = self.parse_multiple_values(row_data["email"])
            row_data["phone"] = self.parse_multiple_values(row_data["phone"])

            yield row_data

    def fetch_sections(self):
        data = self.retrieve_sheet_data(
            sheet_id=self.DOCUMENT_ID,
            sheet_range=self.SECTIONS_RANGE,
        )
        return list(self._sections(data))

    def fetch_persons(self):
        data = self.retrieve_sheet_data(
            sheet_id=self.DOCUMENT_ID,
            sheet_range=self.RANGE,
        )
        return list(self._persons(data))

    def store(self):
        sections_data = self.fetch_sections()
        persons_data = self.fetch_persons()

        with transaction.atomic():
            sections = {}
            for s in sections_data:
                section, _ = TeamSection.objects.update_or_create(
                    code=s["code"].strip(),
                    defaults=dict(
                        name=s["name"].strip(),
                        e_mail=self.take_first(s["email"]).strip(),
                    ),
                )
                sections[section.code] = section

            for p in persons_data:
                person, _ = Person.objects.update_or_create(
                    code=p["code"].strip(),
                    defaults=dict(
                        name=p["name"].strip(),
                        e_mail=self.take_first(p["email"]).strip(),
                        phone=self.take_first(p["phone"]).strip(),
                        city=(p["city"] or "").strip(),
                    ),
                )

                try:
                    section = TeamSection.objects.get(code=p["section"].strip())
                except TeamSection.DoesNotExist:
                    pass
                else:
                    TeamMembership.objects.filter(person=person).delete()
                    TeamMembership.objects.create(section=section, person=person)
