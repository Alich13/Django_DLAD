# Django_DLAD

## Populate db
    python manage.py import_question_csv leran/data/question.csv

## Generate UML
    python manage.py graph_models   -a -I profile,stats,User,Images,Question,Answers_list -o foo_bar.png

## UML Diagram 
![My UML](UML_DB.png)
