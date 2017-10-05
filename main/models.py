from django.db import models

# Create your models here.

class Sogl_uchrej(models.Model):
    sogl = models.IntegerField(verbose_name='Соглашение', blank=True)
    def __str__(self):
        return str(self.sogl)

class Inn_uchrej(models.Model):
    inn = models.CharField(verbose_name='ИНН', blank=True, max_length=11)
    def __str__(self):
        return str(self.inn)

class Uchrejdenie(models.Model):
    name = models.CharField(verbose_name='Наименование', blank=True, max_length=250)
    affiliation = models.CharField(verbose_name='Принадлежность', blank=True, max_length=5)
    def __str__(self):
        return self.name

class Licensee(models.Model):
    name = models.CharField(verbose_name='Наименование', blank=True, max_length=25)
    # date = models.CharField(verbose_name='Дата', blank=True, max_length=25)
    def __str__(self):
        return '{}' .format(self.name)


class Type_uchrej(models.Model):
    type_uch = models.CharField(verbose_name='Тип учреждения', max_length=12)
    def __str__(self):
        return self.type_uch


class State_security(models.Model):
    sogl = models.ForeignKey(Sogl_uchrej, verbose_name='Соглашение')
    inn = models.ForeignKey(Inn_uchrej, verbose_name='ИНН', )
    name = models.ForeignKey(Uchrejdenie, verbose_name='Наименование учреждения', )
    type_uch = models.ForeignKey(Type_uchrej, verbose_name='Тип учреждения', )
    number_PC = models.IntegerField(verbose_name='Количество рабочих мест')
    number_VipNet = models.IntegerField(verbose_name='Количество VipNet')
    number_NSD = models.IntegerField(verbose_name='Количество НСД')
    number_AVPO = models.IntegerField(verbose_name='Количество АВПО')
    certificate = models.CharField(verbose_name='Наличие аттестата', max_length=5)
    date = models.CharField(verbose_name='Дата выдачи аттестата', max_length=10)
    licensee = models.ForeignKey(Licensee, verbose_name='Лицензиат')
    def __str__(self):
        return '{} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {}'.format(
            str(self.sogl), str(self.inn), str(self.name), str(self.type_uch),
            str(self.number_PC), str(self.number_VipNet), str(self.number_NSD),
            str(self.number_AVPO), str(self.certificate), str(self.date), str(self.licensee))
