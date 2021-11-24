![](https://img.shields.io/conda/l/conda-forge/setuptools)
![](https://img.shields.io/pypi/djversions/djangorestframework)

# Django DLAD Quiz
 
## Description
This web application was developed as part of an academic project and is intended for educational purpose .

We Believe that one can learn faster and more efficiently through playing ,thus we developed this web quiz. This platform offers the possibility to users to not only play the quiz game but also explore microscopic images and learn about them .

## Requirements 

All dependencies can be found in <code> ./requirements.txt </code> . otherwise, to make it simple you can just create a conda environment from  <code>./django_environment</code> .     


    conda env create -f django_environment.yml


## Project organisation
3 main django applications where ( learn,quiz and pages ) .
    

    ├── game   
    ├── learn  // static files and code for exploration part ...
    ├── quiz   // static files and code for quiz game  ...
    ├── pages  // static files and code for home, registration ,login ,index page ...
    ├── LICENSE
    ├── manage.py
    ├── Procfile
    ├── db.sqlite3
    ├── django_environment.yml
    ├── README.md
    ├── requirements.txt
    ├── runtime.txt
    ├── staticfiles
    └── UML_DB.png



## Populate db

The process of populating database tables must respect the cardinalities between each table thus populating the \
database can be performed in this order :

1. filling images table 
> python manage.py import_images_csv leran/data/images.csv
2. filling questions table
> python manage.py import_question_csv leran/data/question.csv
3. filling answers table 
> python manage.py import_answers_csv leran/data/answers.csv

the scripts used for these tasks are located in <code> learn/management/commands/ </code>


## UML Diagram
### Generate UML
    python manage.py graph_models   -a -I profile,stats,User,Images,Question,Answers_list -o foo_bar.png

![My UML](UML_DB.png)

