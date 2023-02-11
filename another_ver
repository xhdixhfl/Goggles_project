# library loading
from sentence_transformers import SentenceTransformer models
from ko_sentence_transformers.models import KoBertTransformer
from sentence_transformers import SentenceTransformer, util
import numpy as np
from konlpy.tag import Kkma
import numpy as np
import pandas as pd
import torch

# Model loading
word_embedding_model = KoBertTransformer("monologg/kobert", max_seq_length=75)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(), pooling_mode='mean')
model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

# embedder loading
embedder = SentenceTransformer("jhgan/ko-sbert-sts")

# data loading
df = pd.read_csv('real.csv') 


# corpus & embedding
## 코퍼스 나누기(전체)
## corpus
texts = ''
for line in df.rv[:]:
    texts = texts + line
text = list(filter(None, texts.split(sep='\n')))

## embedding 
tot_corpus = text
tot_embedding = embedder.encode(tot_corpus, convert_to_tensor = True)

# 기초케어 카테고리(bas)
## 범위 split
fir = df[df['cate'] == '토너'].index[0]
las = df[df['cate'] == '미스트'].index[-1]
## corpus
texts = ''
for line in df.rv[fir:las]:
    texts = texts + line
text = list(filter(None, texts.split(sep='\n')))

## embedding
bas_corpus = text
bas_embedding = embedder.encode(bas_corpus, convert_to_tensor = True)

# 색조케어 카테고리(col)
## 범위 split
fir = df[df['cate'] == '립'].index[0]
las = df[df['cate'] == '아이'].index[-1]
## corpus
texts = ''
for line in df.rv[fir:las]:
    texts = texts + line
text = list(filter(None, texts.split(sep='\n')))

## embedding
col_corpus = text
col_embedding = embedder.encode(col_corpus, convert_to_tensor = True)



## 카테고리 분석용 키워드
bas = ['스킨', '스킨로션','로션', '크림','에밀젼','에밀전','에센스','에세스','수분크림',\
       '미스트','촉촉', '세럼','토너','패드','닦토','팩','성분','순한']
col = ['가루','쉐도우','섀도우','새도우','팔레트','파레트','립스틱','립','틴트','발색','매트',\
       '메트','벨벳','밸벳','글로시','입술','글로스','유리알','유리','쿠션','파운','파운데이션',\
       '파데','노세범','파대','밀착력','밀착','컬링','볼륨','롱','마스카라','베이스','속눈썹','컬링력',\
       '아이라인','아이라이너','번지는','유지력', '색']

## konlpy 클래스 호출
kkma = Kkma()

def kst_model(query):
    # 쿼리문에서 카테고리 분석하기
    k = kkma.nouns(query)
    no = [2 if i in bas else 3 if i in col else 1 for i in k]
    answer = [2 if 2 in no and 1 in no else 3 if 3 in no and 1 in no else 1]
    num = answer[0] # 분석된 내용으로 카테고리 선택하기
    if num == 1: # 전체
        embed = tot_embedding
        corpus = tot_corpus

    elif num == 2: # 기초
        embed = bas_embedding
        corpus = bas_corpus

    elif num == 3: # 조색조
        embed = col_embedding
        corpus = col_corpus
        
    # 관련 코퍼스와 임베딩으로 유사 문장 서치
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, embed)[0]
    cos_scores = cos_scores.cpu()  # cpu환경
    
    # 코사인 스코어를 기준으로 top5 산출
    top_results = np.argpartition(-cos_scores, range(5))[0:5]
    answer = [] # 값 담을 리스트
    test = [] # 중복 제거용 리스트
    
    for v, idx in enumerate(top_results[0:5]): 
        text = corpus[idx].strip()
        for i in range(3344):  # 전체 df에서
            if text in df['rv'][i] and text not in test: # 리뷰에 해당하는 내용을 찾아서 이미 찾은 내용인지 판단
                pname = df['pname'][i]
                test.append(text) # answer에 리스트로 업로드해서 리뷰내용만 비교하려고 사용
                answer.append([pname, f"리뷰 내용: {text}", f"(유사도: {round(float(cos_scores[idx]),4)})"])
    return answer
