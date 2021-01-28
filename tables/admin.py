from django.contrib import admin
from .models import BotUsers, BotScheduleUlSTU, BotSchedulePictures, FacultiesULSTU


class BotUsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'group_name', 'faculty')


class BotScheduleUlSTUAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'today', 'tomorrow')


class BotSchedulePicturesAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'picture_weekend_1', 'picture_weekend_2')


admin.site.register(BotUsers, BotUsersAdmin)
admin.site.register(FacultiesULSTU)
admin.site.register(BotSchedulePictures, BotSchedulePicturesAdmin)
admin.site.register(BotScheduleUlSTU, BotScheduleUlSTUAdmin)

