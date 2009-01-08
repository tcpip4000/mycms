from django.contrib import admin
from search.models import SearchKeyword
#from django.contrib.flatpages.models import FlatPage

class SearchKeywordAdmin(admin.ModelAdmin):
    pass
admin.site.register(SearchKeyword, SearchKeywordAdmin)

#class SearchKeywordInline(admin.StackedInline):
#    model = SearchKeyword
#    extra = 3
#admin.site.register(SearchKeyword, SearchKeywordInline)

#class FlatPageAdmin(admin.ModelAdmin):
#    model = FlatPage
#    inlines = [SearchKeywordInline]
#
#admin.site.register(FlatPage, FlatPageAdmin)

