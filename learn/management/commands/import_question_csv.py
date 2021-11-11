import csv
from django.core.management.base import BaseCommand, CommandError
from learn.models import Quiz, Images

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        Quiz.objects.all().delete()
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            header = next(dataReader)
            for row in dataReader:

                q=Quiz(
                    pk = row[0],
                    question=row[1],
                    type = row[2],
                    imagefield =row[3],
                    points = row[4],
                    nb_answers = row[5],
                    nb_images = row[6],
                    time = row[7]
                )
                q.save()
                for img in Images.objects.all():
                    q.images.add(img)


                self.stdout.write(
                    'Created question {} {}'.format(Quiz.type, Quiz.question)
                )
