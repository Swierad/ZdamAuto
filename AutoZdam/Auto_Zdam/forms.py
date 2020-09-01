from django import forms
from django.forms import ModelForm
from .models import Equip, Offer, User





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

class OfferForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
       # user = kwargs.pop('user')
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.fields['user'].initial = user.pk
        self.fields['user'].widget = forms.HiddenInput()


    class Meta:
        model = Offer
        fields = "__all__"
        widgets = {
            'car_equipment': forms.CheckboxSelectMultiple()
        }





class UserCreateForm(forms.ModelForm):
    password2 = forms.CharField(label = 'Password (again)', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'wherefrom']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            msg = 'Podane hasła są różne'
            self._errors['password2'] = self.error_class([msg])
            del self.cleaned_data['password2']

            '''
            Dla non-field error:
            from django.forms.forms import NON_FIELD_ERRORS
            form._errors[NON_FIELD_ERRORS] = form.error_class(['komunikat'])
            '''

        return self.cleaned_data

class UserLoginForm(forms.Form):
    username = forms.CharField(label = 'Login')
    password = forms.CharField(label = 'Hasło', widget = forms.PasswordInput)

class ContactForm(forms.Form):
    description = forms.CharField(label='wiadomość', widget=forms.Textarea)
    price = forms.CharField(label='proponowana cena')

