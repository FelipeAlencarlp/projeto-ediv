from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from tinymce.widgets import TinyMCE
from .uploaded_file import ChunckUploadedFile
from .utils import is_video

def request_budget(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        HTML_FIELD = TinyMCE().render(name='descricao', value='', attrs={'id': 'id_descricao'})
        return render(request, 'request_budget.html', {'HTML_FIELD': HTML_FIELD})
    
    elif request.method == 'POST':
        file = request.POST.get('file')
        if not is_video(file):
            raise HttpResponseBadRequest()

        file_upload = ChunckUploadedFile(file)
        file_upload.save_disk()

        return HttpResponse('teste') 
        

