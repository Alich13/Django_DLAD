import csv
from django.core.management.base import BaseCommand, CommandError
from learn.models import Answer_list ,Question

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        Answer_list.objects.all().delete()
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            header = next(dataReader)
            for row in dataReader:
                print(row[0],row[1],row[2],row[3])
                Answer_list.objects.create(
                    pk = row[0],
                    question_id=Question.objects.get(pk=int(row[1])) ,
                    answer= row[2],
                    definition=row[3],

                )
                # self.stdout.write(
                #     'Created answer {} {}'.format(Answer_list.pk,Answer_list.answer)
                # )
