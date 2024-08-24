from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories(self):
        return Category.objects.all()
    def __str__(self):
        return self.name

class Customsers(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=160)
    password = models.CharField(max_length=100)

    def get_customer_by_email(self):
        try:
            return Customsers.objects.get(email=self.email)
        except Customsers.DoesNotExist:
            return False
    
    def isExist(self):
        if Customsers.objects.get(email=self.email):
            return True
        False

    def register(self):
        self.save()

    def __str__(self):
        return self.name

class Products(models.Model):
    """ some method to retieve product by id, all products, products by category id  """
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=350, null=True, blank=True
    )
    image = models.ImageField(upload_to='store/images', blank=False, null=False)
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.all(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Products.objects.filter(id=category_id)
        else:
            return Products.get_all_products()
        
    
class Orders(models.Model):
    product = models.ForeignKey(
        Customsers, on_delete=models.CASCADE, related_name="productorders"
    )
    customser = models.ForeignKey( 
        Customsers, on_delete=models.CASCADE, related_name="customerorders"
    )
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=59)
    phone = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def placeOrder(self):
        self.save()
    @staticmethod
    def get_order_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by['-date']
    
