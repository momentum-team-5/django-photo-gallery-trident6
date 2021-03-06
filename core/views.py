
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Gallery, Photo
from core.forms import GalleryForm, PhotoForm


def welcome(request):
    if request.user.is_authenticated:
        return redirect(to="gallery_list")
    return render(request, "core/gallery_welcome.html")
    
def gallery_list(request):
    gallerys = request.user.gallerys.all()
    return render(request, "core/gallery_list.html", {"gallerys": gallerys})

def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, id=pk)
    return render(request, "core/gallery_detail.html", {"gallery": gallery})

def gallery_create(request):
    if request.method == "GET":
        form = GalleryForm()
    else:
        form = GalleryForm(data=request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            # check ckeck author or user
            gallery.user = request.user 
            gallery.save()
            return redirect(to="gallery_list")
    return render(request, "core/gallery_create.html", {"form": form}) 

def gallery_delete(request, pk):
    gallery = get_object_or_404(request.user.gallerys.all(), pk=pk)
    gallery.delete()
    return redirect(to="gallery_list")

def photo_add(request, gallery_pk):
    gallery = get_object_or_404(request.user.gallerys, pk=gallery_pk)

    if request.method == "POST":
        form = PhotoForm(data=request.POST, files=request.FILES) # to remove required field
        if form.is_valid():
            photo = form.save(commit=False)
            photo.gallery = gallery
            photo.save()
            return redirect(to="gallery_detail", pk=gallery.pk)
    else:
        form = PhotoForm()

    return render(request, "core/photo_add.html", {
        "form": form,
        "gallery": gallery
    })

def photo_delete(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    photo.delete()
    return redirect(to='gallery_detail', pk=photo.gallery.pk)