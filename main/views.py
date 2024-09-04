from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306152506',
        'name': 'Raihan Akbar',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)



# Create your views here.
