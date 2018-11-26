from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除
    isDelete = models.BooleanField(default=False)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=200,null=True,blank=True)
    # 删除
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey('BookInfo')