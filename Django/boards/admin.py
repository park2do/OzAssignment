from django.contrib import admin
from .models import Board

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass # 이거 등록하면, adminpage에서 보임. 또한, DB에등록하려면 migrations 해줘야함. 파이팅 ㅎㅎ, 

    