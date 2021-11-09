import csv
from django.core.management.base import BaseCommand, CommandError
from learn.models import Question

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            header = next(dataReader)
            for row in dataReader:

                Question.objects.create(
                    pk = row[0],
                    question=row[1],
                    type = row[2],
                    imagefield =row[3],
                    points = row[4],
                    nb_answers = row[6],
                    nb_images = row[5],

                )
                self.stdout.write(
                    'Created question {} {}'.format(Question.type, Question.question)
                )
