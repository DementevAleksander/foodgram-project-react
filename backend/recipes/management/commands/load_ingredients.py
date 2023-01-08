import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from recipes.models import Ingredient, Tag

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'Загрузка перечня ингридиентов из data в формате json.'

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            default='ingredients.json',
            nargs='?',
            type=str
        )

    def handle(self, *args, **options):
        try:
            with open(
                os.path.join(DATA_ROOT, options['filename']),
                'r',
                encoding='utf-8'
            ) as file:
                data = json.load(file)
                for ingredient in data:
                    try:
                        Ingredient.objects.create(
                            name=ingredient['name'],
                            measurement_unit=ingredient['measurement_unit']
                        )
                        self.stdout.write(self.style.SUCCESS('Данные загружены!'))
                    except IntegrityError:
                        print(
                            f'Ингридиет {ingredient["name"]} '
                            f'{ingredient["measurement_unit"]} '
                            f'существует в БД!'
                        )

        except FileNotFoundError:
            raise CommandError('Файл отсутствует в папке data!')
