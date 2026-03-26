from django.contrib import admin
from .models import candidate

@admin.register(candidate)
class CandidateAdmin(admin.ModelAdmin):
    # 1. แสดงคอลัมน์ name และ votes ในหน้าแสดงรายการ
    list_display = ('name', 'votes')
    
    # 2. เพิ่มช่องค้นหาโดยอิงจากชื่อ (ใส่คอมม่าข้างหลังถ้ามีฟิลด์เดียว)
    search_fields = ('name',)
    
    # 3. กำหนดให้ votes เป็นฟิลด์ที่อ่านได้อย่างเดียว (แก้ไขไม่ได้)
    readonly_fields = ('votes',)