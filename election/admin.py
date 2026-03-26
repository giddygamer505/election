from django.contrib import admin
from .models import Candidate, VoteRecord

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    # แสดงรายชื่อ, พรรค (ถ้ามี), และคะแนนโหวต ในหน้า List
    list_display = ('name', 'votes')
    # เพิ่มช่องค้นหาชื่อผู้สมัคร
    search_fields = ('name',)
    # เรียงลำดับตามคะแนนจากมากไปน้อยเป็นค่าเริ่มต้น
    ordering = ('-votes',)

@admin.register(VoteRecord)
class VoteRecordAdmin(admin.ModelAdmin):
    # แสดงเลขไอดี และเวลาที่โหวต
    list_display = ('voter_id', 'timestamp')
    # เพิ่มช่องค้นหาเลขไอดี (สำคัญมากสำหรับตรวจสอบคนโหวตซ้ำ)
    search_fields = ('voter_id',)
    # เพิ่มตัวกรองด้านข้างตามวันเวลา
    list_filter = ('timestamp',)
    # ให้ดูได้อย่างเดียว แก้ไขไม่ได้ (เพื่อความโปร่งใสของผลการเลือกตั้ง)
    readonly_fields = ('voter_id', 'timestamp')

    # ป้องกันไม่ให้ Admin เพิ่ม record เองได้ง่ายๆ ผ่านหน้าเว็บ (Optional)
    def has_add_permission(self, request):
        return False