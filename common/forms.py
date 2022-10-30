from django import forms

class LoginForm(forms.Form):
    user=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"User"}))
    password=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"password","class":"form-control","placeholder":"Password"}))
    remember=forms.BooleanField(required="",widget=forms.CheckboxInput(attrs={"id":"remember"}))