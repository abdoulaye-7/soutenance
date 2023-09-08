from django import forms
from django.forms import ModelForm


from .models import Administratif
from .models import Annee
from .models import Departement
from .models import Filiere
from .models import Niveau
from .models import Classe
from .models import Modul
from .models import Etudiant


class AdminForm(forms.ModelForm):
    class Meta:
        model = Administratif
        fields = "__all__"


class AnnForm(forms.ModelForm):
    class Meta:
        model = Annee
        fields = "__all__"

class DepForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = "__all__"

class FilForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = "__all__"

class NivForm(forms.ModelForm):
    class Meta:
        model = Niveau
        fields = "__all__"

class ClaForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = "__all__"

class ModForm(forms.ModelForm):
    class Meta:
        model = Modul
        fields = "__all__"

class EtuForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = "__all__"










# from django import forms
# from django.forms import ModelForm

# from .models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = "__all__"