from django.contrib import admin
from .models import BoardModel

# Register your models here.
# 管理者側からテーブルのデータが見えるし追加できる
admin.site.register(BoardModel)