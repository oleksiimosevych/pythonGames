from django.contrib import admin
from .models import Document, Project, EzeHersteller, EzeTyp, EzeNeu, EzeBestand
# Register your models here.

admin.site.register(Document)
admin.site.register(Project)
admin.site.register(EzeHersteller)
admin.site.register(EzeTyp)
admin.site.register(EzeNeu)
admin.site.register(EzeBestand)
