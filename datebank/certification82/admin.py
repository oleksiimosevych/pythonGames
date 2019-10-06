from django.contrib import admin
from .models import Document, Project, EzeHersteller,\
 EzeTyp, EzeNeu, EzeBestand, EzeNeuWindkraft, EzeNeuFotovoltaic,\
  EzeNeuGenerator, EzeBestWindkraft, EzeBestFotovoltaic,\
   EzeBestGenerator, Transformator, TrafoTyp, TrafoHersteller,\
    Betreiber, Zertifikatsinhaber, Netzbetreiber, Betreiber2
# Register your models here.

admin.site.register(Document)
admin.site.register(Project)
admin.site.register(EzeHersteller)
admin.site.register(EzeTyp)

# admin.site.register(EzeNeu)
# admin.site.register(EzeBestand)
# admin.site.register(Eze)

admin.site.register(EzeNeuWindkraft)
admin.site.register(EzeNeuFotovoltaic)
admin.site.register(EzeNeuGenerator)

admin.site.register(EzeBestWindkraft)
admin.site.register(EzeBestFotovoltaic)
admin.site.register(EzeBestGenerator)

admin.site.register(Transformator)
admin.site.register(TrafoTyp)
admin.site.register(TrafoHersteller)

admin.site.register(Betreiber)

admin.site.register(Betreiber2)
admin.site.register(Netzbetreiber)

admin.site.register(Zertifikatsinhaber)