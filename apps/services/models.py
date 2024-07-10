from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from tinymce import models as tinymce_models
from datetime import timedelta
from autenticacao.models import Users
from .choices import BudgetStatus, ServiceTags


class Budgets(models.Model):
    client = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(max_length=2, choices=BudgetStatus.choices, default=BudgetStatus.SOLICITADO)
    service_tag = models.CharField(max_length=2, choices=ServiceTags.choices)
    descricao = tinymce_models.HTMLField()
    file_path = models.CharField(max_length=300)

    @property
    def max_date(self):
        return self.data + timedelta(hours=24)
    
    @property
    def urgency(self):
        return mark_safe('<span class="badge bg-danger">Urgente</span>') if timezone.now() > self.max_date else mark_safe('<span class="badge bg-primary">Normal</span>')

    class Meta:
        ordering = ['-data']
