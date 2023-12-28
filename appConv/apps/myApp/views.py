from django_recaptcha.client import RecaptchaResponse
from django.views.generic import FormView
from django.shortcuts import redirect
from .form import LoginMyAppForm


# Create your views here.
class LoginMyApp(FormView):
    template_name = "myApp/app.html"
    form_class = LoginMyAppForm

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get("g-recaptcha-response", "")
        recaptcha_result = RecaptchaResponse(recaptcha_response)

        if recaptcha_result.is_valid:
            client = form.cleaned_data["client"]

            if form.is_valid():
                print(client.web)
                return redirect(client.web)
            

        return super().form_valid(form)
