from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306207663',
        'name': 'Muhammad Abyasa Pratama',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)