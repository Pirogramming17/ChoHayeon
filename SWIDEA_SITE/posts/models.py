from django.db import models

class Devtool(models.Model):
  name = models.CharField(max_length= 50, verbose_name="이름")
  kind = models.CharField(max_length= 50, verbose_name="종류")
  content = models.TextField(verbose_name="내용")

class Post(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    user = models.CharField(max_length= 50, verbose_name="유저이름")
    devtool = models.ForeignKey(Devtool,
                                on_delete=models.CASCADE,
                                related_name="post_devtool")
    content = models.TextField(verbose_name="내용")
    interest = models.IntegerField(verbose_name="관심도")
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name = "사진")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)