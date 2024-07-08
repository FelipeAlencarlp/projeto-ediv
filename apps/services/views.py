from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from .uploaded_file import ChunckUploadedFile
from .utils import is_video

def request_budget(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'request_budget.html')
    
    elif request.method == 'POST':
        file = request.POST.get('file')
        if not is_video(file):
            raise HttpResponseBadRequest()

        file_upload = ChunckUploadedFile(file)
        file_upload.save_disk()

        return HttpResponse('teste') 
        

