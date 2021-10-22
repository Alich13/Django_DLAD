from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from learn.models import *
from django.contrib import messages

def quiz_page(request):
    images = Images.objects.get(pk=1)
    context = {
        "images": images
    }
    return render(request=request,
                  template_name='quiz/quiz_page.html',context=context)