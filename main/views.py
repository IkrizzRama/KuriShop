from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Pistol Air',
        'price': 'Rp.100.000',
        'description': 'Menembakan Air'
    }

    return render(request, "main.html", context)
# Create your views here.
