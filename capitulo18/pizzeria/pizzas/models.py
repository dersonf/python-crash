from django.db import models


class Pizza(models.Model):
    """A topic the user is learning about."""
    name = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """Something specific learned about a topic."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        elif len(self.text) <= 50:
            return f"{self.text}"
