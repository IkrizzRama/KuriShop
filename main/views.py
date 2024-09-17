from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ObjectEntryForm
from main.models import objectEntry

def show_main(request):
    object_entries = objectEntry.objects.all()

    context = {
        'nama' : 'Muhammad Rizky Ramadhani',
        'kelas': 'PBP A',
        'object_entries': object_entries,
    }

    return render(request, "main.html", context)

def create_object_entry(request):
    form = ObjectEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_object_entry.html", context)

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
