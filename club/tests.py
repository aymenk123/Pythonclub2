from django.test import TestCase
from django.contrib.auth.models import User
from .models import PythonType, Product, Review
import datetime
from .forms import ProductFrom
# Create your tests here.
class PythonTypeTest(TestCase):
   def setUp(self):
     self.type=PythonType(typename='Lenovo Laptop')
       

   def test_typestring(self):
       self.assertEqual(str(self.type), 'Lenovo Laptop')

   def test_tablename(self):
       self.assertEqual(str(PythonType._meta.db_table), 'pythontype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=PythonType(typename='Laptop')
        self.user=User(username='user1')
        self.product=Product(productname='Lenovo',producttype=self.type, user=self.user, dateentered=datetime.date(2021,1,10) ,price=1200.99,producturl= 'http://www.lenovo.com', description='lenovo laptop') 

    def test_string(self):
        self.assertEqual(str(self.product), 'Lenovo')

    def test_discount(self):
            disc = self.product.price * .05
            self.assertEqual(self.product.discountAmount(), disc)

    def test_discountedAmount(self):
        disc=self.product.price * (1 -.05)
        self.assertEqual(self.product.discountPrice(),disc)

class NewProductForm(TestCase):
            #valid form data
     def test_productform(self):
        data={
                'productname':'surface',
                'producttype':'laptop',
                'user':'aymen',
                'dateentered': '2021-1-5',
                'price': '1200',
                'producturl': 'http://www.microsoft.com',
                'description':'half laptop half tablet'
            }    
                
        form=ProductForm (data)
        self.assertTrue(form.is_valid)
     #this test is failing
     def test_Productform-Invalid(self):
        
        data={
                'productname':'surface',
                'producttype':'laptop',
                'user':'aymen',
                'dateentered': '2021-1-5',
                'producturl': 'http://www.microsoft.com',
                'description':'half laptop half tablet'
            }  
            
        form=ProductForm (data)
        self.assertFalse(form.is_valid)  