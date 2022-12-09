from django.forms import ValidationError

def validate_phone_number(phone_number:str):
    phone_number = phone_number.replace(' ', '')
    if len(phone_number) != 12:
        raise ValidationError('Длина номера не совпадает!')
    if not phone_number.startswith('+'):
        raise ValidationError('Invalid phone number')
    numbers = '+0987654321'
    for i in phone_number:
        if i not in numbers:
            raise ValidationError(f'Телефонный номер не может содержать "{i}"')

def validate_klas(klass:int):
    if klass > 11:
        raise ValidationError('Такого класса не существует!')