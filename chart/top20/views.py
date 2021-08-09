from django.shortcuts import render


def home(request):
    return render(request, '_common/main_block.html')
