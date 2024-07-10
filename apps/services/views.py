from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.views import View
from tinymce.widgets import TinyMCE
from datetime import datetime
from .uploaded_file import ChunckUploadedFile
from .utils import is_video
from .choices import ServiceTags
from .models import Budgets


class BudgetRequestView(View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        HTML_FIELD = TinyMCE().render(name='descricao', value='', attrs={'id': 'id_descricao'})
        return render(request, 'request_budget.html', {'HTML_FIELD': HTML_FIELD,
                                                       'services': ServiceTags.choices})
    
    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        file = request.FILES.get('file')
        service = request.POST.get('service')
        descricao = request.POST.get('descricao')

        if not is_video(file):
            raise HttpResponseBadRequest()

        file_upload = ChunckUploadedFile(file)
        file_path = file_upload.save_disk()

        budget = Budgets(
            file_path=file_path,
            data=datetime.now(),
            service_tag=service,
            descricao=descricao,
            client=request.user
        )
        budget.save()

        #TODO: Redirecionar para visualização do status do orçamento
        messages.add_message(request, messages.SUCCESS, mark_safe('Orçamento solicitado com sucesso. <a href="#">Clique aqui</a> para ver o status.'))
        return redirect(reverse('request_budget')) 
