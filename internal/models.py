from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.
class Incident(models.Model):
    Location_CHOICES=[
        ("1","Corporate HeadOfiice"),
        ("2","Operation Department"),
        ("3","Work station"),
        ("4","Marketing Division")
    ]
    Severity_CHOICES=[
        ("1","Mild"),
        ("2","Moderate"),
        ("3","Severe"),
        ("4","Fatal")
    ]


    location=models.CharField(_("Location"), choices=Location_CHOICES,blank=False,max_length=100,default="1")
    description=models.TextField(_("Incident department"),blank=False)
    time=models.DateTimeField(_("Date and Time"), auto_now=False, auto_now_add=False,blank=False)
    incident_location=models.TextField(_("Incident Location"),help_text="where did it happend in the company")
    severity=models.CharField(_("Initial severit"), choices=Severity_CHOICES,blank=False,max_length=100,default="1")
    cause=models.TextField(_("Suspected Cause"))
    action_taken=models.TextField(_("immediate action taken"))
    environmental=models.BooleanField(_("Enviromental Incident"),default=False)
    injury_illnes=models.BooleanField(_("Injury/Illnes"),default=False)
    property_damage=models.BooleanField(_("Property Damage"),default=False)
    vehicle=models.BooleanField(_("Vehicle"),default=False)
    reported_by=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Reported By"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
