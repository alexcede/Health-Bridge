from api.models.admin.model import Admin
from api.models.user_support.model import UserSupport
from api.models.user.model import User
from api.models.doctor.model import Doctor

def validate_unique_fields(data):
    unique_errors = {}

    try:
        # Verificar el email
        email = data.get('email')
        if email:
            for model in [Admin, UserSupport, User, Doctor]:
                if model.objects.filter(email=email).exists():
                    unique_errors['email'] = "El email ya está en uso."

        # Verificar el DNI
        dni = data.get('dni')
        if dni:
            for model in [User, Doctor]:
                if model.objects.filter(dni=dni).exists():
                    unique_errors['dni'] = "El DNI ya esta en uso."

        # Verificar el número de teléfono
        phone_number = data.get('phoneNumber')
        if phone_number:
            for model in [UserSupport, User, Doctor]:
                if model.objects.filter(phoneNumber=phone_number).exists():
                    unique_errors['phoneNumber'] = "El número de teléfono ya está en uso."

        healthCardCode = data.get('healthCardCode')
        if healthCardCode:
            for model in [User]:
                if model.objects.filter(healthCardCode = healthCardCode).exists():
                    unique_errors['healthCardCode'] = "El numero de la tarjeta ya esta en uso."

    except Exception as e:
        # Capturar cualquier excepción y devolver un error genérico
        unique_errors['__all__'] = "Ocurrió un error al validar los campos únicos."

    return unique_errors