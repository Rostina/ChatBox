from django import forms

from chat.models import FriendMessage, Profile


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class MessageForm(forms.ModelForm):
    title = forms.ChoiceField(choices=(('complaint', 'compliant'), ('request', 'request'), ('praise', 'praise'), ('job', 'job')))
    class Meta:
        model = FriendMessage
        fields = ["title", "message"]

    def clean(self):
        cleaned_data = super().clean()


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Profile
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
        username = cleaned_data.get('first_name') + " " + cleaned_data.get('last_name')

        if email != verify_email:
            raise forms.ValidationError("You must enter the same email in both fields")

        if password != verify_password:
            raise forms.ValidationError("You must enter the same password in both fields")

        if username == "ChatBox staff" or username == "No One":
            raise forms.ValidationError("sorry that username is reserved to the ChatBox staff")
        elif Profile.objects.filter(username=username).exists() and Profile.objects.filter(password=password).exists():
            raise forms.ValidationError(
                """Your name and/or password is already used by another person (different people)
                Change a little your name or password"""
            )


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

