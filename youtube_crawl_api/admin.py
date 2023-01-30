from django.contrib import admin

from .models import Video

# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ("added_to_db",)


admin.site.register(Video, RatingAdmin)
