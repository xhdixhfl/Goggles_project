# torch.save
## 직렬화된 객체를 디스크에 저장하는 함수. python의 pickle을 사용하여 직렬화함
## 모든 종류의 객체모델, tensor 및 딕셔너리를 저장 할 수 있음 

# library loading
from sentence_transformers import SentenceTransformer models
from ko_sentence_transformers.models import KoBertTransformer
from sentence_transformers import SentenceTransformer, util
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
### data폴더의 MDdata.cs정설정
df = pd.read_csv('real.csv') 


# corpus & embedding
## 전체 카테고리
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

# modeul save
torch.save({'df':df, 'embedder':embedder, 'word_embedding_model':word_embedding_model,'pooling_model':pooling_model,\
            'model':model,'tot_corpus':tot_corpus, 'tot_embedding':tot_embedding, 'bas_corpus':bas_corpus,\
            'bas_embedding':bas_embedding, 'col_corpus':col_corpus, 'col_embedding':col_embedding}, "info.tar")
