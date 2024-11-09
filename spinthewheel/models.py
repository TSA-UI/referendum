from django.db import models
from django.contrib.auth.models import User
from explore.models import Menu

# Option to be put on the wheel
class Option(models.Model):
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE)
    added = models.BooleanField(default=False)

# Save history after spinning
class SpinHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    winner = models.TextField()
    spin_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu} - {self.spin_time}"
    

