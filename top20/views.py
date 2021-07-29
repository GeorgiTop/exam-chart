from django.shortcuts import render


def home(request):
    # songs = Songs.objects.all()
    # context = {
    #     'songs': songs
    # }
    return render(request, 'index.html')
# Create your views here.
