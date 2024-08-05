from django.db import models

# Create your models here.

COLORS = (
    ('black', 'Black'),
    ('blue', 'Blue'),
    ('brown', 'Brown')
    )

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
    ('XXXL', 'Extra Extra Extra Large')
    
)


SEASONS = (
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winter')
)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Setting(BaseModel):
    logo = models.ImageField(upload_to='logo/')
    slider_image1 = models.ImageField(upload_to='slider/')
    slider_image2 = models.ImageField(upload_to='slider/')
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    bitcoin_card = models.CharField(max_length=19, null= True, blank= True)
    americanExpress_card = models.CharField(max_length=19,null= True, blank=True)
    paypal_card = models.CharField(max_length=19, null= True, blank=True)
    master_card = models.CharField(max_length=19, null= True, blank= True)
    visa_card = models.CharField(max_length=19, null= True, blank= True)

    def __str__(self):
        return "Setting's object"
    
class Product(BaseModel):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(upload_to='product/')
    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    description = models.TextField(max_length=500, null= True, blank=True)
    rating = models.IntegerField(default=0)
    colors = models.CharField(choices=COLORS, max_length=10)
    sizes = models.CharField(choices=SIZES, max_length=10)
    seasons = models.CharField(choices=SEASONS, max_length=10)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')


class Blog(BaseModel):
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title
    

class Contact(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name


        
