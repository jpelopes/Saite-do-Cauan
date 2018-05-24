from django.db import models
from django.core.validators import RegexValidator

class BackgroundImage(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='background')

    def __str__(self):
        return self.name

class Settings(models.Model):
    name = models.CharField(max_length=40)
    background_image = models.ForeignKey(BackgroundImage, on_delete=models.SET_NULL, blank=True, null=True)
    background_color = models.CharField(max_length=6, validators=[RegexValidator('^[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e ,f]{6}$')], default='ffffff')
    menu_font = models.URLField(default='https://fonts.googleapis.com/css?family=Karla:400,400i,700,700i')
    menu_font_color = models.CharField(max_length=6, validators=[RegexValidator('^[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e ,f]{6}$')], default='ffffff')
    menu_font_color_hover = models.CharField(max_length=6, validators=[RegexValidator('^[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e ,f]{6}$')], default='fc4620')
    page_font = models.URLField(default='https://fonts.googleapis.com/css?family=Karla:400,400i,700,700i')
    page_font_color = models.CharField(max_length=6, validators=[RegexValidator('^[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e ,f]{6}$')], default='000000')

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails')
    show = models.BooleanField(default=True)
    settings = models.ForeignKey(Settings, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='photos')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bio(models.Model):
    text = models.TextField(max_length=500)

    def __str__(self):
        return 'Bio'

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Bio, self).save(*args, **kwargs)

class Page(models.Model):
    name = models.CharField(max_length=15)
    settings = models.ForeignKey(Settings, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
