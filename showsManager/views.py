from django.shortcuts import render, redirect
from .models import shows

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
    NewShow = shows.objects.create(title = request.POST['Title'], network = request.POST['Network'], releasedDate = request.POST['releaseDate'], discription = request.POST['Discription'])
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