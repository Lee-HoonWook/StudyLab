from re import compile, match

# 욕이 들어간 메모 삭제
def check_memo():

    from core.models import Memos

    # 모든 메모의 content 수집
    memos = Memos.objects.all().only('content')

    # 한국어 욕 정규표현식
    p = compile(
        '[시씨슈쓔쉬쉽쒸쓉]([0-9]*|[0-9]+ *)[바발벌빠빡빨뻘파팔펄]|[섊좆좇졷좄좃좉졽썅춍]|ㅅㅣㅂㅏㄹ?|ㅂ[0-9]*ㅅ|[ㅄᄲᇪᄺᄡᄣᄦᇠ]|[ㅅㅆᄴ][0-9]*[' +
        'ㄲㅅㅆᄴㅂ]|[존좉좇][0-9 ]*나|[자보][0-9]+지|보빨|[봊봋봇봈볻봁봍] *[빨이]|[후훚훐훛훋훗훘훟훝훑][장앙]|후빨|[엠앰]창|애[미비]|애자|[^탐]색기' + 
        '|([샊샛세쉐쉑쉨쉒객갞갟갯갰갴겍겎겏겤곅곆곇곗곘곜걕걖걗걧걨걬] *[끼키퀴])|새 *[키퀴]|[병븅]신|미친[가-닣닥-힣]|[믿밑]힌|[염옘]병|[샊샛샜샠섹섺셋셌셐' + 
        '셱솃솄솈섁섂섓섔섘]기|[섹섺섻쎅쎆쎇쎽쎾쎿섁섂섃썍썎썏][스쓰]|지랄|니[애에]미|갈[0-9]*보[^가-힣]|[뻐뻑뻒뻙뻨][0-9]*[뀨큐킹낑)|꼬추|곧휴|[가-힣]슬아' + 
        '치|자박꼼|[병븅]딱|빨통|[사싸](이코|가지|까시)|육시[랄럴]|육실[알얼할헐]|즐[^가-힣]|찌(질이|랭이)|찐따|찐찌버거|창[녀놈]|[가-힣]{2,}충[^가-힣]|' + 
        '[가-힣]{2,}츙|부녀자|화냥년|환[양향]년|호[구모]|조[선센][징]|조센|[쪼쪽쪾]([발빨]이|[바빠]리)|盧|무현|찌끄[레래]기|(하악){2,}|하[앍앜]|[낭당랑' + 
        '앙항남담람암함][ ]?[가-힣]+[띠찌]|느[금급]마|文在|在寅|(?<=[^\n])[家哥]|속냐|[tT]l[qQ]kf|Wls')

    # 삭제될 메모 모음
    delete_memos = list(filter(lambda m : m if match(p, m.content) else '', memos))

    # 욕이 들어간 메모 삭제
    list(map(lambda d : d.delete(), delete_memos))

    # print('delete logs')