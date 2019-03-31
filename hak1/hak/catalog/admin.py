from django.contrib import admin
from .models import Action, Problem, Face1, Representative, Partner, PartnerIndividual
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class ActionAdmin(admin.ModelAdmin):
    list_display = ('action_name', 'action_period')
    date_hierarchy = 'action_period'


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('goal', 'first_name', 'second_name', 'third_name', 'need_time')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification_number')
    list_filter = ('tag',)


class PartnerIndividualAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'third_name', 'number', 'email')
    list_filter = ('tag', 'second_name')


# Register your models here.
admin.site.register(Action, ActionAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Representative)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerIndividual, PartnerIndividualAdmin)
