from django.shortcuts import render, redirect
from kobert.models import DBdata
import kst_function as model

# 상품 등록
def home(request):
    items = DBdata.objects.order_by('pname')
    texts = DBdata.objects.order_by('review')

    return render(request, 'kobert/home.html',
                  {'products':len(items), 'review_count': len(texts)})

  
# query 받기
def transfer(request):
    text = request.POST.get('query')
    trans_info = {
        'review': text
    }
    return render(request, 'kobert/detail.html', trans_info)
  
  
# 모델 실행
def kst_model(request):    # 원소별로 리스트 저장한 함수 부른거
    if request.method == 'POST':
        query = str(request.POST.get('query'))
        answer = model.kst(query)

    info = {
            'query': query,
            'answer': answer
        }
    return render(request, 'kobert/test2.html', info)
