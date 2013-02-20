from django.contrib import admin
from djangor.models import Books

# class ChoiceInline(admin.TabularInline):
#   model = Choice
#   extra = 3
#   ordering = ('choice',)
#   

class BookAdmin(admin.ModelAdmin):
  list_display = ('pub_date','title','author','isbn','publisher')
  list_filter = ('pub_date', )
  ordering = ('pub_date', )
#   inlines = (ChoiceInline,)

admin.site.register(Books,BookAdmin)
# admin.site.register(Choice)