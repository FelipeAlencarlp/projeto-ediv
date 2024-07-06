from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Users
from .active_account import ActiveAccount

@receiver(post_save, sender=Users)
def active_account_mail(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        active_account = ActiveAccount(instance)
        active_account.active_account_send_mail()