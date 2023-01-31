from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
   ('dresses', 'dresses'),
    ('shirts', 'shirts'),
    ('jeans', 'jeans'),
    ('swimwear', 'swimwear'),
    ('sleepwear','sleepwear'),
    ('sportswear', 'sportswear'),
    ('jumpsuits', 'jumpsuits'),
    ('blazers', 'blazers'),
    ('jackets', 'jackets'),
    ('shoes', 'shoes')
)
    

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    image=models.ImageField(default='fashion.jpg', upload_to='album_pictures')
    price=models.FloatField()
    discount= models.PositiveIntegerField(null=True, blank=True)
    discount_price=models.PositiveIntegerField(null=True, blank=True)
    selling_price=models.FloatField(null=True, blank=True)

    @property
    def discount_price(self):
        return ((self.price)*(self.discount))/100
    
    @property
    def selling_price(self):
        return (self.price)-(self.discount_price)
    

    class Meta:
        verbose_name_plural = 'Clothes'


    def __str__(self):
        return self.name


   