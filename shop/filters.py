from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PriceRangeFilter(admin.SimpleListFilter):
    title = _('price range')
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('0-100', _('From $0 to $100')),
            ('101-500', _('From $101 to $500')),
            ('501-1000', _('From $501 to $1000')),
            ('1001-more', _('More than $1001')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-100':
            return queryset.filter(price__gte=0, price__lte=100)
        if self.value() == '101-500':
            return queryset.filter(price__gte=101, price__lte=500)
        if self.value() == '501-1000':
            return queryset.filter(price__gte=501, price__lte=1000)
        if self.value() == '1001-more':
            return queryset.filter(price__gte=1001)