from django.db.models.signals import post_save, post_delete
from .models import Specialskills, Week
from django.dispatch import receiver

@receiver(post_save,sender=Specialskills)
def autogenerateproject(sender,instance,created,**kwargs):
    print("signal fire automatic")
    if created:
        projectdata = instance
        # print(projectdata.name)
        # print(projectdata.techstack)
        # print(projectdata.description)
        # print(projectdata.link)
        Week.objects.create(
            name = projectdata.name,
            Day = projectdata.Day,
        )

        print("week created")


@receiver(post_delete,sender=Specialskills)
def autospecialskillsgone(sender,instance,**kwargs):
        projectdata = instance
        print(projectdata.name)
        fdata = Week.objects.get(name=projectdata.name)
        fdata.delete()
    