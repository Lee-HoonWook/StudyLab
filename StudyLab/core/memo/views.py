from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.memo.forms import MemoForm
from core.utils import check_token


# 메모 작성 = 로그인 시 페이지 접근 가능
@login_required
def memo_create(request):

    # sidebar active
    nav_check = 'sidebar_memo'

    # 메모 폼
    form = MemoForm()

    # Token
    token = check_token(request)

    return render(request, 'memo/create.html', {'nav_check' : nav_check, 'form' : form, 'token' : token})

# 메모 리스트 보기
def memo_list(request):

    # sidebar active
    nav_check = 'sidebar_memo'

    # 페이지 구현
    page = int(request.GET.get('p', 1))

    return render(request, 'memo/list.html', {'nav_check' : nav_check, 'page' : page})

# 메모 상세보기
def memo_view(request):

    # sidebar active
    nav_check = 'sidebar_memo'

    return render(request, 'memo/retrieve.html', {'nav_check' : nav_check})

# 메모 수정 = 로그인 시 페이지 접근 가능
@login_required
def memo_update(request):

    # sidebar active
    nav_check = 'sidebar_memo'

    # Token
    token = check_token(request)

    return render(request, 'memo/update.html', {'nav_check' : nav_check, 'token' : token})

# 메모 검색
def memo_find(request):

    # sidebar active
    nav_check = 'sidebar_memo'

    # 키워드 및 값 받아오기
    relation = request.GET.get('relation', '내용')
    key = request.GET.get('key', '')

    # 페이지 구현
    page = int(request.GET.get('p', 1))

    return render(request, 'memo/find.html', {
        'nav_check': nav_check, 'key': key, 'relation': relation, 'page' : page
    })