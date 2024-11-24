from django.db import models



class ABitInfoAboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return 'Немного информации о нас'
    

class SlogansNumbers(models.Model):
    our_slogan = models.ForeignKey('OurSlogan', on_delete=models.CASCADE,
                                    related_name='slogans_numbers', null=True, blank=True)
    number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.text
    

class SlogansText(models.Model):
    our_slogan = models.ForeignKey('OurSlogan', on_delete=models.CASCADE,
                                    related_name='slogans_text', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class OurSlogan(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.title
    

class ProudRewards(models.Model):
    image = models.ImageField(upload_to='proud/')
    description = models.CharField(max_length=255)
    our_proud = models.ForeignKey('OurProud', on_delete=models.CASCADE,
                                   related_name='proud_rewards', null=True, blank=True)

    def __str__(self):
        return self.description
    

class OurProud(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
    

class CompanyAuthors(models.Model):
    name = models.CharField(max_length=255)
    company_authors_info = models.ForeignKey('CompanyAuthorsInfo', on_delete=models.CASCADE,
                                             related_name='company_authors', null=True, blank=True)
    url_1 = models.URLField(null=True, blank=True)
    url_2 = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class CompanyAuthorsInfo(models.Model):
    image = models.ImageField(upload_to='authors/')
    description = models.TextField()

    def __str__(self):
        return self.description