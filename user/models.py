from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = (
    (1,'male'),
    (0,'famale')
)
class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    nike_name = models.CharField(verbose_name='昵称', max_length=50, default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_CHOICES, null=True)
    address = models.CharField(verbose_name='地址',max_length=100, default='')
    mobile = models.CharField(verbose_name='电话号码', max_length=11, unique=True, null=False)
    head_img = models.ImageField(upload_to='')

    def __repr__(self):
        return self.username
