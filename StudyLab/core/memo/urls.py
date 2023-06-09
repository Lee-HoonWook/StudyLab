from django.urls import path
from core.memo.views import *

urlpatterns = [
    # 메모 작성
    path('write', memo_create, name='m-write'),

    # 메모 리스트
    path('list', memo_list, name='m-list'),

    # 메모 상세보기
    path('view', memo_view, name='m-view'),

    # 메모 수정
    path('rewrite', memo_update, name='m-rewrite'),

    # 메모 검색
    path('find', memo_find, name='m-find')
]