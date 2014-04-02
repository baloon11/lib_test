# coding: utf-8
from django.db import models

class Author(models.Model):    
    first_last_name = models.CharField(u'Фамилия Имя Отчество',max_length=1000) 

    def __unicode__(self):
        return '%s %s'% (self.id,self.first_last_name)
        
    class Meta:
        verbose_name_plural = "Aвторы"


class Book(models.Model):    
    title= models.CharField(u'Название книги',max_length=250)
    author = models.ManyToManyField(Author,verbose_name=u'Автор(ы)') 

    def __unicode__(self):
        return '%s %s'% (self.id,self.title)

    def get_absolute_url(self):   
        return "/book/%i/" %self.id     
      
    class Meta:
        verbose_name_plural = "Книги"
