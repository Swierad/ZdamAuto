from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _



DOORS_NUMBER = (
    (1, "3"),
    (2, "5"),
)

SEATS_NUMBER = (
    (1, "2"),
    (2, "4"),
    (3, "5"),
    (4, "6")
)

FUEL_TYPE = (
    (1, "benzyna"),
    (2, "diesel"),
    (3, "LPG"),
    (4, "benzyna/lpg"),
    (4, "hybryda"),
    (4, "elektryczny")
)

CATEGORY = (
    (1, "osobowe"),
    (2, "dostawcze"),
    (3, "motocykl")
)

TYPE = (
    (1, "SUV"),
    (2, "sedan"),
    (3, "hatchback")
)

EQUIP = (
    (1, "ABS"),
    (2, "Elektryczne lusterka przednie"),
    (3, "Bluetooth"),
    (4, "ESP (stabilizacja toru jazdy)"),
    (5, "Czujniki parkowania"),
    (6, "Elektrycznie ustawiane fotele"),
    (7, "Światła LED"),
    (8, "CD "),
    (9, "Podgrzewane lusterka boczne"),
    (10, "Podgrzewane przednie siedzenia"),
    (11, "klimatyzacja"),
    (12, "Kurtyny powietrzne"),
    (13, "Isofix "),
    (14, "elektryczne lusterka tylne"),
    (15, "Centralny zamek "),
    (16, "Czujnik zmierzchu"),
    (17, "Komputer pokładowy"),
    (18, "System Start-Stop"),
    (19, "Czujnik deszczu"),
    (20, "Alarm"),
    (21, "Wielofunkcyjna kierownica"),
    (22, "Klimatyzacja automatyczna"),
    (23, "Elektryczne szyby przednie"),
    (24, "Elektryczne szyby tylne"),
    (25, "ASR (kontrola trakcji)"),
    (26, "Kamera cofania"),
    (27, "Elektrochromatyczne lusterko wsteczne"),
    (28, "Tempomat"),
    (29, "Nawigacja GPS"),
    (30, "Immobilizer"),
    (31, "Alufelgi"),


)

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    wherefrom = models.CharField(max_length=64)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def __str__(self):
        return self.email


class Equip(models.Model):
    equip = models.CharField(max_length=64)

    def __str__(self):
        return self.equip


class Offer(models.Model):
    car_brand = models.CharField(max_length=64, verbose_name="Marka")
    car_model = models.CharField(max_length=64, verbose_name="Model")
    category = models.IntegerField(choices=CATEGORY, verbose_name="Kategoria")
    type = models.IntegerField(choices=TYPE, verbose_name="Typ")
    year_of_production = models.SmallIntegerField(verbose_name="Rok produkcji")
    color = models.CharField(max_length=64, verbose_name="Kolor")
    car_mileage = models.IntegerField(verbose_name="Przebieg")
    description = models.TextField(verbose_name="Opis")
    car_equipment = models.ManyToManyField(Equip, verbose_name="Wyposażenie")
    fuel_type = models.IntegerField(choices=FUEL_TYPE, verbose_name="Rodzaj paliwa")
    doors_number = models.IntegerField(choices=DOORS_NUMBER, verbose_name="Liczba drzwi")
    seats_number = models.IntegerField(choices=SEATS_NUMBER, verbose_name="Liczba siedzeń")
    engine_capacity = models.IntegerField(verbose_name="Pojemność silnika")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Wystawiający")
    price = models.IntegerField(verbose_name="Cena")
    photos = models.ImageField(upload_to='media')
    photos_2 = models.ImageField(upload_to='media', null=True, blank= True)
    photos_3 = models.ImageField(upload_to='media', null=True, blank= True)
    photos_4 = models.ImageField(upload_to='media', null=True, blank= True)
    photos_5 = models.ImageField(upload_to='media', null=True, blank= True)


    def __str__(self):
        return self.car_brand + " " + self.car_model


