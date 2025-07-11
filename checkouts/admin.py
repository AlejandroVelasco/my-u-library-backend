from django.contrib import admin
from .models import Checkout

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "checked_out_at", "returned_at")
    list_filter = ("returned_at",)
    search_fields = ("user__username", "book__title")
