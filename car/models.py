from django.db import models



class User(models.Model):
    phone = models.CharField(max_length=255, unique=True, default=None)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}: {self.phone}'


class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'


class AutoModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.brand} {self.name}'

class Auto(models.Model):
    STATUSES = (
        ('1', 'FREE'),
        ('2', 'BOOKED'),
        ('3', 'TAKEN'),
    )
    vin_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=1, choices=STATUSES, default='1')

    auto_model = models.ForeignKey('AutoModel', on_delete=models.CASCADE)

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, default=None)



    def __str__(self):
        return f'{self.auto_model} vin: {self.vin_code}'



class Image(models.Model):
    title = models.CharField(max_length=255)
    url_image = models.ImageField(upload_to='image')


    def __str__(self):
        return f'{self.title}'

# Create your models here.
