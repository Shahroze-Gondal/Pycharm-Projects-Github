from django import forms

# import GeeksModel from models.py
from form_app.models import UseModel


# create a ModelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = UseModel
        fields = "__all__"

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
