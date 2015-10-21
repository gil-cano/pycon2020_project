from django.contrib import admin
from .models import Talk
from .models import Track


class TalkInline(admin.StackedInline):
    '''
        Stacked Inline View for Talk
    '''
    model = Talk


class TrackAdmin(admin.ModelAdmin):
    inlines = [TalkInline, ]

admin.site.register(Talk)
admin.site.register(Track, TrackAdmin)
