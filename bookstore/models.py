from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    comment   = models.TextField()
    date      = models.DateTimeField(default=timezone.now)
    owner_name= models.ForeignKey(User, on_delete=models.CASCADE)
    image     = models.ImageField(default='default.jpg', upload_to='profile_pics')
    contact_no= models.PositiveIntegerField(default=91)
    price     = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
    	return reverse('book-content', kwargs = {'pk':self.pk})