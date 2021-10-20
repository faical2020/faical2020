from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from prod.models.preprod import Preprod
# Register your models here.

@admin.register(Preprod)
class PreprodAdmin(ImportExportModelAdmin):
    pass
