from django.db import models


class Collaborator(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    title = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', default='defaultpp.jpg', blank=True, null=True)
    education_bs = models.CharField(max_length=100, blank=True, null=True)
    education_master = models.CharField(max_length=100, blank=True, null=True)
    education_phd = models.CharField(max_length=100, blank=True, null=True)
    current_departmant = models.CharField(max_length=100, blank=True, null=True)
    current_university = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    detailed_cv = models.URLField(blank=True, null=True)
    resarch_interest = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    room_number = models.CharField(max_length=100, blank=True, null=True)
    rank = models.IntegerField(default='1', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now_add=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        ordering = ["rank"]
    
    def __str__(self):
        return self.name
    

class Researcher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    title = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', default='defaultpp.jpg', blank=True, null=True)
    education_bs = models.CharField(max_length=100, blank=True, null=True)
    education_master = models.CharField(max_length=100, blank=True, null=True)
    education_phd = models.CharField(max_length=100, blank=True, null=True)
    current_departmant = models.CharField(max_length=100, blank=True, null=True)
    current_university = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    detailed_cv = models.URLField(blank=True, null=True)
    resarch_interest = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    room_number = models.CharField(max_length=100, blank=True, null=True)
    rank = models.IntegerField(default='1', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now_add=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        ordering = ["rank"]
    
    def __str__(self):
        return self.name
