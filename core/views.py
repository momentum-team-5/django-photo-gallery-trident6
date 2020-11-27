
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Gallery, Photo


def welcome(request):
    return render(request, "core/gallery_welcome.html")

def gallery_list(request):
    gallerys = request.user.gallerys.all()
    return render(request, "core/gallery_list.html", {"gallerys": gallerys})

def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, id=pk)
    return render(request, "core/gallery_detail.html", {"gallery": gallery})