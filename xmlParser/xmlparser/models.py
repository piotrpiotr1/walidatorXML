from django.db import models


class Files(models.Model):
    name = models.CharField(verbose_name='Nazwa pliku', max_length=40)
    file = models.FileField(verbose_name='Plik', upload_to='xmlparser/files')

    class Meta:
        verbose_name_plural = 'Pliki'

    def __str__(self):
        return self.name

