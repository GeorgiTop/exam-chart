from django.shortcuts import render


def home(request):
    # songs = Songs.objects.all()
    # context = {
    #     'songs': songs
    # }
    return render(request, '_common/main_block.html')
# Create your views here.
