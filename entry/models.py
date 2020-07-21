from django.db import models
from django.contrib.auth.models import User

# # Create your models here.


def user_directory_path(instance, filename):
    return 'buildings/user_{0}/{1}'.format(instance.user.id, 'facade1.jpg')


def user_directory_path1(instance, filename):
    return 'buildings/user_{0}/{1}/{2}'.format(instance.user.username, instance.title, 'facade1.jpg')


def user_directory_path2(instance, filename):
    return 'buildings/user_{0}/{1}/{2}'.format(instance.user.username, instance.title, 'facade2.jpg')


def user_directory_path3(instance, filename):
    return 'buildings/user_{0}/{1}/{2}'.format(instance.user.username, instance.title, 'facade3.jpg')


def user_directory_path4(instance, filename):
    return 'buildings/user_{0}/{1}/{2}'.format(instance.user.username, instance.title, 'facade4.jpg')
# def user_directory_pathb(instance, filename):
#     return 'buildings/user_{0}/{1}'.format(instance.user.id, 'facade2')
# def user_directory_pathc(instance, filename):
#     return 'buildings/user_{0}/{1}'.format(instance.user.id, 'facade3')
# def user_directory_pathd(instance, filename):
#     return 'buildings/user_{0}/{1}'.format(instance.user.id, 'facade4')


class Entry(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name='oluşturan')
    # username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, related_name='kullanıcıadı')
    title = models.CharField(
        max_length=100, verbose_name='Başlık', blank=True, null=True)
    content = models.TextField(
        max_length=100, verbose_name='Açıklama', blank=True, null=True)
    city = models.CharField(
        max_length=100, verbose_name='Şehir', blank=True, null=True)
    district = models.CharField(
        max_length=100, verbose_name='İlçe', blank=True, null=True)
    neighborhood = models.CharField(
        max_length=100, verbose_name='Mahalle', blank=True, null=True)
    zipcode = models.CharField(
        "ZIP / Postal code", max_length=12, blank=True, null=True)
    adress = models.TextField(verbose_name='Açık Adres', blank=True, null=True)
    facade1 = models.ImageField(
        upload_to=user_directory_path1, default='defaultbuilding.jpg', blank=True, null=True)
    facade2 = models.ImageField(
        upload_to=user_directory_path2, default='defaultbuilding.jpg', blank=True, null=True)
    facade3 = models.ImageField(
        upload_to=user_directory_path3, default='defaultbuilding.jpg', blank=True, null=True)
    facade4 = models.ImageField(
        upload_to=user_directory_path4, default='defaultbuilding.jpg', blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Güncellenme Tarihi")
    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='Düzenleyen')
    # created_by = models.ForeignKey(
    #     User, to_field="username", on_delete=models.SET_NULL, null=True, blank=True, related_name='Oluşturan')
    

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.title
