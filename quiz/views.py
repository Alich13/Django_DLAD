from django.shortcuts import render
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *


def index(request):
    return render(request=request ,
                  template_name= 'quiz/index.html')

@login_required(login_url='/')
def home(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    # # then format the request.
    # # note that we don't use album['name'] anymore but album.name
    # # because it's now an attribute.
    # formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    # message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    context ={"albums": albums}
    return render(request=request ,
                  template_name= 'quiz/home.html',
                  context=context)

# Create your views here.

def listing(request):
    album_list = Album.objects.filter(available=True)
    paginator = Paginator(album_list, 2)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    context = {
        "albums": albums,
               'paginate': True
               }
    return render(request=request,
                  template_name='quiz/listing.html',
                  context=context)

def detail(request, album_id):

    album = Album.objects.get(pk=album_id) #primary key = album_id(qui vient de l'url)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    context ={
        "album" : album ,
        "artists" : artists

    }
    return render(request=request,
                  template_name='quiz/details.html',
                  context=context)


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s" % query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'quiz/search.html', context)
