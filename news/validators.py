from django.core.exceptions import ValidationError


def validate_min_two_words(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
