import csv
from django.core.management.base import BaseCommand, CommandError
from learn.models import Images

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            header = next(dataReader)
            for row in dataReader:
                print(row[0], row[1],row[7])
                Images.objects.create(
                    pk = row[0],
                    name = row[1],
                    description = row[2],
                    microscopy = row[3],
                    cell_type = row[4],
                    component = row[5],
                    doi = row[6],
                    organism = row[7]
                )
                self.stdout.write(
                    'Created employee {} {}'.format(Images.name, Images.doi)
                )
