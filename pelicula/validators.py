from django.core.exceptions import ValidationError
import re

def validar_only_text(value):
    patron = r'^[a-zA-Z]+$'
    if not bool(re.match(patron, value)):
        raise ValidationError(f"El valor solo debe contener letras", params={ 'value': value } )


def validar_calificacion(value):
    patron = r'^(100(\.0{1,2})?|[1-9]?\d(\.\d{1,2})?)$'
    if not bool(re.match(patron, value)):
        raise ValidationError(f"El valor solo debe contener numeros del 1 al", params={ 'value': value } )
    

