from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class meta(UserCreationForm.meta):
        fields = UserCreationForm.meta.fields + ("email",)