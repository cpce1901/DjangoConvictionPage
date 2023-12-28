from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings
from .models import Clients




class LoginMyAppForm(forms.Form):

    client = forms.ModelChoiceField(
        label= "Cliente",
        queryset=Clients.objects.all(),
        empty_label="Seleccionar cliente",
        widget=forms.Select(
            attrs={
                "id": "client",
                "class": "text-input-select"
            }
        )
    ) 

    recaptcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV2Checkbox(),
        error_messages={"required": settings.RECAPTCHA_ERROR_MSG["required"]},
    )

    