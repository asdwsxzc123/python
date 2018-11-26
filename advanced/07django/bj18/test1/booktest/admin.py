from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# Register your models here.
# 自定义管理模型
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'btitle', 'bpub_date']
# class HeroInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'btitle', 'bpub_date']
# 注册模型类
# admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
# admin.site.register(HeroInfo,HeroInfoAdmin)