import os
import magic

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from AudioClassification.functions import *

media_dir = settings.MEDIA_ROOT


def home(request):
    return render(request, "home.html")


def result(request):
    context = {}
    if request.method == "POST":
        file = request.FILES.get("wavfile")
        if file is None:
            context["error_message"] = "Please select a file."
            return render(request, "home.html", context)
        
        file_type = magic.from_buffer(file.read(), mime=True)
        if not file_type.startswith("audio/"):
            context["error_message"] = "Invalid file type. Only audio files are allowed."
            return render(request, "home.html", context)
            
        tmp = file.name
        print("The File Name is --> ", tmp)
        fs = FileSystemStorage()
        name = fs.save(file.name, file)
        audio_path = str(media_dir) + str(name)
        print("File Saved and its path is --> ", str(media_dir) + str(name))
        context["ANN_Prediction"] = ANN_print_prediction(audio_path)
        context["CNN1D_Prediction"] = CNN1D_print_prediction(audio_path)
        context["CNN2D_Prediction"] = CNN2D_print_prediction(audio_path)
        print("ANN Predicted --> ", ANN_print_prediction(audio_path))
        print("CNN1D Predicted --> ", CNN1D_print_prediction(audio_path))
        print("CNN2D Predicted --> ", CNN2D_print_prediction(audio_path))
        return render(request, "result.html", context)
    else:
        return render(request, "home.html")
