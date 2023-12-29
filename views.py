import os
from django.http import JsonResponse
from django.shortcuts import render
from .models import Folder
from django.core.files.base import ContentFile

def handle_folder_upload(request):
    upload_directory = 'uploads/'
    os.makedirs(upload_directory, exist_ok=True)

    if request.method == 'POST':
        uploaded_folder = request.FILES.getlist('folder')

        for uploaded_file in uploaded_folder:
            content_file = ContentFile(uploaded_file.read(), name=uploaded_file.name)
            folder_instance = Folder(
                folder_name=uploaded_file.name, 
                uploaded_file=content_file
            )
            folder_instance.save()

        return JsonResponse({'message': 'Folder uploaded successfully'})

    directory_contents = os.listdir(upload_directory)
    return render(request, 'members/folder_upload.html', {'directory_contents': directory_contents})
