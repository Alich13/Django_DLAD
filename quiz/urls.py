from django.conf.urls import url
from django.urls import path
from . import views # import views so we can use them in urls.

app_name = 'quiz'

urlpatterns = [
    path('<pk>/', views.quiz_page , name="quiz_page"),
    path('<pk>/data/', views.quiz_data_view, name='quiz-data-view'),
    path('<pk>/save/', views.res_view),
]