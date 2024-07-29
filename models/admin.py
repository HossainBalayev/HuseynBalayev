from django.contrib import admin
from models.models import Setting, Category, Product, Blog

admin.site.register(Setting)

admin.site.register(Category)

admin.site.register(Blog)

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',"created_at",)
    search_fields = ('name',)
    list_per_page = 20
    readonly_fields = ['view', 'like']
    list_display_links = ('name',)


admin.site.site_header = "Huseyn's Project"


    



   
