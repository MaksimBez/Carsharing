from django.contrib import admin
from car.models import Brand, Auto, AutoModel, Image, User
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'booked_auto', )
    search_fields = ('phone',)


    def booked_auto(self, instance):
        auto = Auto.objects.filter(user__name=instance.name)
        if not auto:
            return None
        return auto.get()



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', )
    ordering = ('name', )

    readonly_fields = ('preview', )

    def preview(self, instance: Brand):
        if not instance.image:
            return mark_safe(f'<b>without logo</b>')
        return mark_safe(f'<image src="/media/{instance.image.url_image}" width="40" height="30">')


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('auto_model', 'vin_code', 'status', )
    list_filter = ('status', 'auto_model', )
    search_fields = ('vin_code', )
    ordering = ('auto_model__brand', )




@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'count_of_auto')
    list_filter = ('brand',)
    ordering = ('name',)

    def count_of_auto(self, instance):
        count = Auto.objects.filter(auto_model__name=instance.name).count()
        return count


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', )

# Register your models here.
