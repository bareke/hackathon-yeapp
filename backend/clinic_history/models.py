from django.db.models import Model
from django.db.models import JSONField
from django.db.models import DateTimeField

# Create your models here.


class ClinicHistory(Model):
    """Clase que representa una historia clínica"""

    data = JSONField(default=dict, help_text='historia clínica')
    created_at = DateTimeField(
        auto_now_add=True,
        help_text='fecha de creación'
    )
    updated_at = DateTimeField(
        auto_now=True,
        help_text='fecha de actualización'
    )
    
    class Meta:
        verbose_name_plural = "Clinic histories"

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """
        return self.created_at.strftime('%a %H:%M  %d/%m/%y')
