from django.core.exceptions import ValidationError


def check_space(value) -> None:
    if ' ' in value:
        raise ValidationError('Имя не может содержать пробелы')