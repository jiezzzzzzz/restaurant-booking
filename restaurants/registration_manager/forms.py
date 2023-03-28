from django import forms
from .models import Manager


class ManagerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Manager
        fields = ['id_manager', 'login', 'password', 'email', 'surname', 'name', 'patronymic']
        labels = {
            'id_manager': 'Код менеджера',
            'login': 'Логин',
            'password': 'Пароль',
            'email': 'Email',
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Manager.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')
        return email

    def save(self, commit=True):
        manager = super().save(commit=False)
        manager.set_password(self.cleaned_data['password'])
        if commit:
            manager.save()

        return manager
