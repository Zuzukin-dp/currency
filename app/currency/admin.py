from django.contrib import admin
from currency.models import ContactUs, Rate, Source

from rangefilter.filters import DateTimeRangeFilter

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RateResource(resources.ModelResource):
    class Meta:
        model = Rate


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'cur_type',
        'source',
        'created',
    )
    list_filter = (
        ('created', DateTimeRangeFilter),
        'cur_type',
        'source',
        'created',
    )
    search_fields = (
        'cur_type',
        'source',
    )
    readonly_fields = (
        'buy',
        'sale',
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Rate, RateAdmin)


class SourceResource(resources.ModelResource):
    class Meta:
        model = Source


class SourceAdmin(ImportExportModelAdmin):
    resource_class = SourceResource
    list_display = (
        'id',
        'name',
        'url',
        'phone',
        'created',
        'updated',
    )
    list_filter = (
        'name',
        ('created', DateTimeRangeFilter),
        ('updated', DateTimeRangeFilter),
    )
    search_fields = (
        'name',
        'phone',
    )
    readonly_fields = (
        'created',
        'updated',
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Source, SourceAdmin)


class ContactUsResource(resources.ModelResource):
    class Meta:
        model = ContactUs


class ContactUsAdmin(ImportExportModelAdmin):
    resource_class = ContactUsResource
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
        'created',
    )
    list_filter = (
        ('created', DateTimeRangeFilter),
    )
    search_fields = (
        'email_from',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)
