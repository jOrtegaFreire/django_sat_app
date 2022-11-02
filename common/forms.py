from django import forms

class LoginForm(forms.Form):
    user=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"User"}))
    password=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"password","class":"form-control","placeholder":"Password"}))
    remember=forms.BooleanField(required="",widget=forms.CheckboxInput(attrs={"id":"remember"}))

class AddComponentForm(forms.Form):
    component_code=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Component Code"}))
    component_qty=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"number","class":"form-control","placeholder":"Component Quantity"}))
    component_price=forms.CharField(label="",help_text="",widget=forms.NumberInput(attrs={"type":"number","class":"form-control","placeholder":"Component Price"}))
    component_description=forms.CharField(label="",help_text="",widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Component Description"}))
    
class EditComponentFormHelper(forms.Form):
    component_code=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","hidden":"True"}))

class EditComponentForm(forms.Form):
    component_code=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Component Code","readonly":"True"}))
    component_qty=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"number","class":"form-control","placeholder":"Component Quantity"}))
    component_price=forms.CharField(label="",help_text="",widget=forms.NumberInput(attrs={"type":"number","class":"form-control","placeholder":"Component Price"}))
    component_description=forms.CharField(label="",help_text="",widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Component Description"}))

class UserRegisterForm(forms.Form):
    user_username=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Username"}))
    user_first_name=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Firs Name"}))
    user_last_name=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Last Name"}))
    user_email=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"email","class":"form-control","placeholder":"Email"}))
    user_password1=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"password","class":"form-control","placeholder":"Password"}))
    user_password2=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"password","class":"form-control","placeholder":"Password"}))
    

class CheckClientForm(forms.Form):
    client_id=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"10.123.123-1"}))

class NewClientForm(forms.Form):
    client_id=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Client Id","readonly":"True"}))
    first_name=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Firs Name"}))
    last_name=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Last Name"}))
    email=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"email","class":"form-control","placeholder":"Email"}))
    phone_number=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Phone Number"}))
    
class NewIngressForm(forms.Form):
    # client info
    client_id=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Client Id","readonly":"True"}))
    first_name=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Firs Name","readonly":"True"}))
    last_name=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"user","class":"form-control","placeholder":"Last Name","readonly":"True"}))
    email=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"email","class":"form-control","placeholder":"Email"}))
    phone_number=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Phone Number"}))
    #ingres info
    ingress_date=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control datetimepicker-input","placeholder":"DD/MM/YY","data-target":"#reservationdate"}))
    failure_description=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Failure description"}))
    inspection_status=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Inspection Status"}))
    accessories=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Accessories"}))

    #appliance info
    appliance_type=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Appliance type"}))
    appliance_brand=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Appliance brand"}))
    appliance_model=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Appliance model"}))
    appliance_sn=forms.CharField(label="",help_text="",widget=forms.TextInput(attrs={"type":"text","class":"form-control","placeholder":"Appliance S/N"}))

# class EditComponentForm(forms.Form):
#     component_id=forms.CharField(label="",help_text="",widget=forms.NumberInput(attrs={"type":"number",""}))
