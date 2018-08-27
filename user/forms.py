from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#giriş formumuz
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label = "Kullanıcı Adı")
    password = forms.CharField(max_length=20, label = "Parola", widget = forms.PasswordInput)



#kayıt olma formu
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,help_text="Zorunludur.", label="Adınız")
    last_name = forms.CharField(max_length=30, required=False, help_text='İsteğe bağlıdır.', label= "Soyadınız")
    email = forms.EmailField(max_length=254, help_text='Geçerli bir e-mail adresi girin.') 

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email', 'password1', 'password2', )


class logout(forms.Form):
    pass
