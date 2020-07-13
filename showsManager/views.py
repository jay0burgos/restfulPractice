from django.shortcuts import render, redirect
from .models import shows
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'shows': shows.objects.all(),
    }
    return render(request, 'index.html', context)

#link that
def newShow(request):
    return render(request, 'newShow.html')

def createNewShow(request):
    #error validation
    errors = shows.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')

    NewShow = shows.objects.create(title = request.POST['title'], network = request.POST['network'], releasedDate = request.POST['releaseDate'], discription = request.POST['discription'])
    return redirect('/shows/' + str(NewShow.id))
# title = models.CharField(max_length = 255)
#     network = models.CharField(max_length = 255)
#     releasedDate = models.DateField()
#     discription = models.TextField()
def displayShow(request, showId):
    show = shows.objects.get(id = showId)
    context = {
        'show' : show
    }
    return render(request, 'displayShow.html', context)

def editShow(request, showId):
    show = shows.objects.get(id = showId)
    context = {
        'show' : show
    }
    return render(request, 'editShow.html', context)

#set edits
def setEdit(request, showId):
    show = shows.objects.get(id = showId)

    show.title = request.POST['Title']
    show.network = request.POST['Network']
    show.releaseDate = request.POST['releaseDate']
    show.discription = request.POST['Discription']
    show.save()

    return redirect('/shows/' + str(show.id))

def delete(request, showId):
    show = shows.objects.get(id = showId)
    show.delete()
    return redirect('/shows')