from django.forms import ValidationError


def brand_validate(brand):
    available_brands = ('Toyota', 'Niva', 'Zhiga', 'Nivasik', 'VAZic')

    if brand not in available_brands:
        raise ValidationError('Not available Brand')

    return True
