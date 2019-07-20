from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movie, Genre

# Giving the admin website access to the Genre model
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    pass

# Giving the admin website access to the Movie model
@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    pass

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class MyModelAdmin(ReadOnlyAdmin):
    pass