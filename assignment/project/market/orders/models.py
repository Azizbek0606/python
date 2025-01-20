from django.db import models
from users.models import Users
from products.models import Product

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending",
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.id} - {self.customer.user.username}"

    def update_status(self, new_status):
        allowed_transitions = {
            "pending": ["processing", "cancelled"],
            "processing": ["completed", "cancelled"],
            "completed": [],
            "cancelled": [],
        }

        if new_status in allowed_transitions[self.status]:
            self.status = new_status
            self.save()
        else:
            raise ValueError(f"Cannot change status from {self.status} to {new_status}")


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        return self.quantity * self.price

    def upadate_quantity(self, new_quantity):
        if int(new_quantity) > 0:
            self.quantity = int(new_quantity)
            self.save()
        else:
            raise ValueError("Quantity must be a positive integer")
    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
