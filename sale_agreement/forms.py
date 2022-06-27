from django import forms
from sale_agreement.models import User


class FormDangKy(forms.ModelForm):
    user_id = forms.CharField(label='User ID', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "user_id",
    }))
    user_name = forms.CharField(max_length=20, label='Username', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Username",
    }))
    user_password = forms.CharField(max_length=100, label='Mật khẩu', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Mật khẩu",
    }))
    xac_nhan_password = forms.CharField(max_length=100, label='Xác nhận mật khẩu', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Xác nhận mật khẩu",
    }))
    user_full_name = forms.CharField(max_length=300, label='Full name', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Full name",
    }))
    user_title = forms.CharField(max_length=100, label='Title', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Title",
    }))
    user_mobile_1 = forms.CharField(max_length=20, label='Điện thoại 1', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Điện thoại",
    }))
    user_mobile_2 = forms.CharField(max_length=20, label='Điện thoại 2', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Điện thoại",
    }))
    user_email = forms.EmailField(max_length=50, label='Email', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Email",
    }))
    created_by = forms.IntegerField(label='Created By', widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "created_by",
    }))

    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'user_password', 'user_full_name', 'user_title', 'user_mobile_1','user_mobile_2','user_email']


class FormDoiMatKhau(forms.ModelForm):
    mat_khau_hien_tai = forms.CharField(label='Mật khẩu hiện tại', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Mật khẩu hiện tại",
    }))
    user_password = forms.CharField(label='Mật khẩu mới', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Mật khẩu mới",
    }))
    xac_nhan_mat_khau = forms.CharField(label='Xác nhận Mật khẩu', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Xác nhận Mật khẩu",
    }))

    class Meta:
        model = User
        fields = ['mat_khau_hien_tai', 'user_password', 'xac_nhan_mat_khau']

