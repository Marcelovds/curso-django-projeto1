import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from recipes.models import Recipe


def delete_foto(instance):
    try:
        os.remove(instance.foto.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=Recipe)
def recipe_foto_delete(sender, instance, *args, **kwargs):
    old_instance = Recipe.objects.filter(pk=instance.pk).first()

    if old_instance:
        delete_foto(old_instance)


@receiver(pre_save, sender=Recipe)
def recipe_foto_update(sender, instance, *args, **kwargs):
    old_instance = Recipe.objects.filter(pk=instance.pk).first()

    if not old_instance:
        return

    is_new_foto = old_instance.foto != instance.foto

    if is_new_foto:
        delete_foto(old_instance)
