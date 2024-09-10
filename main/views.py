from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'E-Commerce App',
        'your_name': 'Geordie',
        'class_name': 'PBP'
    }
    return render(request, 'home.html', context)

