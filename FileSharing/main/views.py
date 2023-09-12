from os import listdir

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from FileSharing.settings import BASE_DIR, MEDIA_ROOT


def upload(request):
    context = {}
    fs = FileSystemStorage()
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = [{'url':fs.url(name), 'name' : name} for name in listdir(MEDIA_ROOT)]

    return render(request, 'upload.html', context)