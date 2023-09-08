from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Student, Teacher, Adminis, Question, Answer, Lesson, Comment
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


# ***********************************************************registering the  new formgroup************************************
#from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group


# #User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
       model = Group
       exclude = []
   # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
         # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk)
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance

# ***********************************************************************

# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)

#  ****************************************************student signup form******************************

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    nom = forms.CharField(widget=forms.TextInput())
    prenom = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()
    tel = forms.CharField(widget=forms.TextInput())
    annEntre = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        student = Student.objects.create(user=user, nom=self.cleaned_data.get('nom'),
                                         prenom=self.cleaned_data.get('prenom'), email=self.cleaned_data.get('email'),
                                         tel=self.cleaned_data.get('tel'), annEntre=self.cleaned_data.get('annEntre'))
        return user

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    nom = forms.CharField(widget=forms.TextInput())
    prenom = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()
    tel = forms.CharField(widget=forms.TextInput())
    subject = forms.CharField(widget=forms.TextInput())


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        teacher = Teacher.objects.create(user=user, nom=self.cleaned_data.get('nom'), prenom=self.cleaned_data.get('prenom'), email=self.cleaned_data.get('email'), tel=self.cleaned_data.get('tel'), subject=self.cleaned_data.get('subject'))
        return user

class AdminisSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    nom = forms.CharField(widget=forms.TextInput())
    prenom = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()
    tel = forms.CharField(widget=forms.TextInput())
    annEmploi = forms.CharField(widget=forms.TextInput())


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_adminis = True
        if commit:
            user.save()
        adminis = Adminis.objects.create(user=user, nom=self.cleaned_data.get('nom'),
                                         prenom=self.cleaned_data.get('prenom'), email=self.cleaned_data.get('email'),
                                         tel=self.cleaned_data.get('tel'), annEmploi=self.cleaned_data.get('annEmploi'))
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Question
        fields = ('question',)


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Answer
        fields = ('answer',)


class LessonForm(forms.ModelForm):
    lesson = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Lesson
        fields = ('lesson',)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ('comment',)