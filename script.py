import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

from classmates_cards.models import ClassmateData
from data import dataset as dts


if __name__ == '__main__':
    ClassmateData.objects.all().delete()

    for key, value in dts.items():
        for item in value:
            ClassmateData.objects.create(
                id=key,
                last_name=item["last_name"],
                first_name=item["first_name"],
                country=item["country"],
            )
