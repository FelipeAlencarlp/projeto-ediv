from django.db import models
from tinymce import models as tinymce_models
from autenticacao.models import Users
from .choices import BudgetStatus, ServiceTags


class Budgets(models.Model):
    client = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(max_length=2, choices=BudgetStatus.choices, default=BudgetStatus.SOLICITADO)
    service_tag = models.CharField(max_length=2, choices=ServiceTags.choices)
    descricao = tinymce_models.HTMLField()
    file_path = models.CharField(max_length=300)
