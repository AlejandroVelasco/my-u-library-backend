from django.conf import settings
from django.db import models

class Checkout(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="checkouts",
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="checkouts",
    )
    checked_out_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_returned(self):
        return self.returned_at is not None

    def __str__(self):
        status = "Returned" if self.is_returned else "Out"
        return f"{self.user.username} → {self.book.title} ({status})"
