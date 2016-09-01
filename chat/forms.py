from django import forms

from chat import models


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = models.Profile
        fields = ["first_name", "last_name", "phone",
              "email", "birthday", "gender", "picture"
              ]
    verify_email = forms.EmailField(max_length=150, label="Verify your email address")
    password = forms.CharField(widget=forms.PasswordInput)
    verify_password = forms.CharField(max_length=20, label="Please verify your password",
                                          widget=forms.PasswordInput)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="leave empty",
                               validators=[must_be_empty],
                               )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')

        if email != verify_email:
            raise forms.ValidationError("You must enter the same email in both fields")

        if password != verify_password:
            raise forms.ValidationError("You must enter the same password in both fields")


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label="full name:  ")
    email = forms.EmailField(max_length=254, label="Email:  ")
    password = forms.CharField(widget=forms.PasswordInput)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="leave empty",
                               validators=[must_be_empty],
                               )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')


class ChatPostForm(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = ['image', 'title', 'text', 'share']

    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="leave empty",
                               validators=[must_be_empty],
                               )

    def clean(self):
        cleaned_data = super().clean()


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = ['image', 'text']

    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="leave empty",
                               validators=[must_be_empty],
                               )

    def clean(self):
        cleaned_data = super().clean()





