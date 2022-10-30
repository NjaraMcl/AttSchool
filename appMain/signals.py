from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from appMain.models import Teacher, Classe, Eleve
from django.contrib.auth import get_user_model


User = get_user_model()


@receiver(post_delete, sender=Eleve)
def delete_eleve_user(sender, instance, **kwargs):
    User.objects.filter(pk=instance.user.pk).delete()


@receiver(post_delete, sender=Teacher)
def delete_eleve_user(sender, instance, **kwargs):
    User.objects.filter(pk=instance.t_user.pk).delete()
