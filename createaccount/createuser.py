class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput())
    

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist : 
            return self.cleaned_data['username']
        raise forms.ValidationError("This username is taken")

    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("passwords don't match")
        return self.cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'], password = self.clean_data['password'])

        new_user.save();

        new_person = Person.objects.create_person(firstname=self.cleaned_data['firstname'], lastname=self.cleaned_data['lastname'], username=self.cleaned_data['username'])

        return new_person



