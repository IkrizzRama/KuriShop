from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ObjectEntryForm
from main.models import objectEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/login')
def show_main(request):
    object_entries = objectEntry.objects.all()

    context = {
        'nama' : 'Muhammad Rizky Ramadhani',
        'kelas': 'PBP A',
        'npm'  : '2306240143',
        'object_entries': object_entries,
        'last_login' : request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_object_entry(request):
    form = ObjectEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_object_entry.html", context)

def register(request):
    form = UserCreationForm()

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = objectEntry.objects.all()

def show_xml(request):
    data = objectEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = objectEntry.objects.all()

def show_json(request):
    data = objectEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = objectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = objectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
