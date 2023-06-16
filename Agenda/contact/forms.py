from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date', )
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'phone': 'Telefono',
            'mobile': 'Numero de Celular',
            'email': 'Correo',
            'company': 'Compañia',
            'notes': 'Notas',
        }

        