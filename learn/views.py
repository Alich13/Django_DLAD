from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.http import JsonResponse

def My_paginetor(request, items, nb_items_in_page):
    paginator = Paginator(items, nb_items_in_page)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return items




@login_required
def All_resources(request):
    images = Images.objects.all()
    results_found = str(len(images))
    images = My_paginetor(request, images, 9)
    context = {
        "images": images,
        'results_found': results_found,
        'paginate': True
    }
    return render(request=request,
                  template_name='learn/listing.html',
                  context=context)


#

@login_required
def detail(request, image_id):
    image = Images.objects.get(id=image_id)  # primary key = album_id(qui vient de l'url)

    context = {
        "image": image,
        "doi_url": image.doi.split(":")[1]
    }
    return render(request=request,
                  template_name='learn/details.html',
                  context=context)


@login_required
def search(request):
    query = request.GET.get('query')
    if not query:
        images = Images.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        images = Images.objects.filter(
            Q(microscopy__icontains=query) |
            Q(cell_type__icontains=query) |
            Q(organism__icontains=query)
        )
    if not images.exists():
        images = Images.objects.filter(description__icontains=query)
    title = "Résultats pour la requête : ' %s '" % query
    results_found = str(len(images))
    images = My_paginetor(request, images, 9)
    context = {
        'images': images,
        'title': title,
        'results_found': results_found,
        'paginate': True
    }
    return render(request, 'learn/search.html', context)

#
def autocomplete(request):
    #print (request.GET("term"))

    returned_terms = []
    if 'term' in request.GET:
        qs_microscopy=Images.objects.filter(
            microscopy__icontains=request.GET.get('term')
        )
        qs_cellType = Images.objects.filter(
            cell_type__icontains=request.GET.get('term')
        )
        qs_org = Images.objects.filter(
            organism__icontains=request.GET.get('term')
        )

        returned_terms = []
        for element in qs_microscopy:
            returned_terms.append(element.microscopy )

        for element in qs_cellType:
            returned_terms.append(element.cell_type )

        for element in qs_org:
            returned_terms.append(element.organism)

        returned_terms = list(dict.fromkeys(returned_terms)) #remove duplicates
        print (returned_terms)


    return JsonResponse(returned_terms,safe=False)

    # return render(request,'pages/templates/pages/home.html')