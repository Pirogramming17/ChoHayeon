from django.db import models

# Create your models here.
class Comment(models.Model):
    user_id = models.CharField(default="user_id",  blank=True, null=False, max_length=40, verbose_name="유저아이디")
    content = models.TextField(verbose_name="내용")
    like = models.BooleanField(default=False, verbose_name="좋아요")