from django.shortcuts import render
from django.http import HttpResponse

import cv2
from .forms import ImageUploadForm
from .models import ImageUpload
from django.urls import reverse_lazy # new
import imageio

import pytesseract as tess
from PIL import Image

def read_view(request):
    form=ImageUploadForm()
    text=None
    instance=None
    all_data=None
    language='ben'
    upload_msg=None
    if request.method == 'POST':
        form=ImageUploadForm(request.POST, request.FILES)
        
        if form.is_valid():          
           data = form.save()
           path = data.image
           all_data = ImageUpload.objects.all()
           instance=ImageUpload.objects.get(id=data.id)
           update_path = instance.image.path 
           img=Image.open(update_path) 
           language=request.POST.get('language')
           print(language)
           text=tess.image_to_string(img,lang=language)
           instance.text=text
           instance.save()
           upload_msg=1


    return render(request,'home.html',{'form':form,'text':text,'current_img':instance,'all_img':all_data,'up_msg':upload_msg})


# Create your views here.
