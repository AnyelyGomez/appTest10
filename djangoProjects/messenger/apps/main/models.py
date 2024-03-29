from django.db import models
from ckeditor.fields import RichTextField

class manager(models.Model):
    id=models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    create_date = models.DateField('Create date', auto_now=False, auto_now_add=True)
    modify_date = models.DateField('Modify date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Delete date', auto_now=True, auto_now_add=False)
    class Meta:
        abstract = True
        
class social(models.Model):
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    class Meta:
        abstract=True

class Category(manager):
    name = models.CharField('name', max_length=150, unique=True)
    image = models.ImageField('Image', upload_to = 'category/')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
         return self.name


class Author(manager, social):
    firsthame = models.CharField('First name', max_length=150)
    lastname = models.CharField('lastname', max_length=150)
    email = models.CharField('E-mail', max_length=200)
    description = models.TextField('Description')
    image = models.ImageField('Author image', null=True, blank=True, upload_to='authors/')
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
         return '{0}{1}{2}', format(self.lastname, " ", self.firsthame)

class Post(manager):
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField()
    image = models.ImageField('Image', upload_to = 'image/', max_length=200)
    published = models.BooleanField('Published / No published', default=False)
    published_date = models.DateField('Publishet date')
    class Meta:
        verbose_name ='Post'
        verbose_name_plural='Posts'
    def __str__(self):
        return self.title   

class Web(manager, social):
    about_us = models.TextField('About us')
    phone = models.CharField('Phone', max_length=10) 
    email= models.EmailField('E-mail', max_length=20)
    class Meta:
        verbose_name='web'
        verbose_name_plural = 'webs'
    def __str__(self):
        return self.about_us

class SocialNectworks(manager, social):
    class Meta:
        verbose_name ='social network'
        verbose_name_plural = 'social networks'
    def __str__(self):
        return self.facebook  
class Contact(manager):
    firstname = models.CharField('Firstname', max_length = 100)
    lastname= models.CharField('Lastname', max_length = 100)
    email = models.EmailField('E-mail', max_length = 150 )
    subject = models.EmailField('Subject', max_length = 100)
    message = models.TextField('Message')
    class Meta: 
        verbose_name ='Contact'
        verbose_name_plural = 'Contacts'
    def __str__(self):
        return self.subject

class Suscriber(manager):
    email = models.EmailField('E-mail', max_length = 150)
    class Meta: 
        verbose_name ='Suscriber'
        verbose_name_plural = 'Suscriber'
    def __str__(self):
        return self.email