from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "name",
                "placeholder": "Ingresa un nombre",
                "class": "text-input",
            }
        ),
    )

    email = forms.EmailField(  # Cambiado a EmailField para validar correos electrónicos
        label="Correo electrónico",
        max_length=100,
        widget=forms.EmailInput(  # Cambiado a EmailInput
            attrs={
                "id": "email",
                "placeholder": "Ingresa un correo",
                "class": "text-input",
            }
        ),
    )

    code = forms.CharField(
        min_length=3,
        label="Codigo",
        max_length=4,
        widget=forms.TextInput(
            attrs={
                "id": "code",
                "placeholder": "+56",
                "class": "text-input-1",
            }
        ),
    )

    phone = forms.CharField(
        min_length=6,
        label="Teléfono",
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "id": "phone",
                "placeholder": "Ingresa un teléfono",
                "class": "text-input-2",
            }
        ),
    )

    address = forms.CharField(
        label="Dirección",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "id": "address",
                "placeholder": "Ingresa una dirección",
                "class": "text-input",
            }
        ),
    )

    details = forms.CharField(
        label="Detalles",
        max_length=512,
        widget=forms.Textarea(
            attrs={
                "id": "details",
                "rows": 8,
                "placeholder": "Ingresa los detalles porfavor...",
                "class": "text-input",
            }
        ),
    )

    recaptcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV2Checkbox(),
        error_messages={"required": settings.RECAPTCHA_ERROR_MSG["required"]},
    )

    def clean_phone(self):
        numero = self.cleaned_data["phone"]

        # Verificar si la entrada consiste solo en dígitos
        if not numero.isdigit():
            raise forms.ValidationError("Ingrese solo números...")

        return numero

    def clean_code(self):
        code = self.cleaned_data["code"]

        if "+" not in code[0]:
            raise forms.ValidationError("Ingresa un código de país valido... ")
        elif not code[1:-1].isdigit():
            raise forms.ValidationError("Ingrese los números del código de su país... ")
        return code