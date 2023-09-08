from django.contrib import admin

# Register your models here.
from .models import Administratif
from .models import Etudiant
from .models import Annee
from .models import Classe
from .models import Modul
from .models import Niveau
from .models import Filiere
from .models import Departement

admin.site.register(Administratif)
admin.site.register(Etudiant)
admin.site.register(Annee)
admin.site.register(Classe)
admin.site.register(Modul)
admin.site.register(Niveau)
admin.site.register(Filiere)
admin.site.register(Departement)



# from django.contrib import admin
# from .models import Task
# # Register your models here.

# admin.site.register(Task)