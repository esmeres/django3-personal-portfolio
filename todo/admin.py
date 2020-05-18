from django.contrib import admin
from .models import Todo

#for us to add the read only field "created"
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register (Todo,TodoAdmin)
