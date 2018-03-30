from django.db import models

class Books(models.Model):
    book_name= models.CharField(max_length=120)
    def __str__(self):
        return self.book_name


class Auther(models.Model):
    auther = models.ForeignKey(Books, on_delete = models.CASCADE)
    auther_name = models.CharField(max_length=120)
    auther_book_price= models.CharField(max_length=1500)
    auther_img= models.FileField()
    def __str__(self):
        return self.auther_name

