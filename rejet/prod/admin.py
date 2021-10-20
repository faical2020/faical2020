from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol
# Register your models here.

@admin.register(Preprod)
class PreprodAdmin(ImportExportModelAdmin):
    pass

@admin.register(Qcontrol)
class QcontrolAdmin(ImportExportModelAdmin):
    pass

