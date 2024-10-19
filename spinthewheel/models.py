from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu.name

class SpinHistory(models.Model):
    selected_option = models.ForeignKey(Menu, on_delete=models.CASCADE)
    spin_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.selected_option.name} - {self.spin_time}"
