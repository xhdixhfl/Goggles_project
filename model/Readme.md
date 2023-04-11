# Ko-Sentence-Bert(transformers)
### 시행 배경
> 상품을 통해 얻고 싶은 정보가 무엇일지 고민함<br>
> 사고자 하는 목적에 맞는 제품을 편리하게 찾을 방법을 고민함

### 기능
- 파이썬 트랜스포머 모듈 이용
- 리뷰쿼리속 단어들을 기반으로 카테고리를 분류하여 코퍼스와 임베딩 그룹을 선택하여 진행함 <br>
※ 코사인 유사도를 토대로 판정함
- 리뷰쿼리 검색을 통해 유사도 높은 리뷰들을 추출해줌

### 사용 언어 및 도구
<img src="http://img.shields.io/badge/Python-3776AB?style=round&logo=Python&logoColor=white" /><img src="http://img.shields.io/badge/PyTorch-EE4C2C?style=round&logo=PyTorch&logoColor=white" /><img src="http://img.shields.io/badge/Jupyter-F37626?style=round&logo=Jupyter&logoColor=white" /><img src="http://img.shields.io/badge/GitHub-181717?style=round&logo=GitHub&logoColor=white" />

※ Ko-Sentence_bert와 KoNLPY를 베이스로 함
![019](https://user-images.githubusercontent.com/114147352/230918869-9cf820ef-72d6-46d5-9171-03debfffdfc6.jpg)

![020](https://user-images.githubusercontent.com/114147352/230919125-224a402c-bff7-48d8-87c1-da25aed9d87a.jpg)
----
<h2> 파일 설명</h2>
<h3>
1. <a href="https://github.com/xhdixhfl/Goggles_project/blob/main/model/another_ver.py">another_ver</a> 
</h3>
→ 입력받은 리뷰쿼리가 konlpy를 통과하면서 토큰이 분리되고 토큰을 토대로 카테고리를 선택하여 카테고리에 맞는 DB속 상품데이터를 기반으로 해당 상품의 리뷰 중 검색 쿼리와 가장 유사한 리뷰를 추출해 주는 API <br>
  <img src="https://user-images.githubusercontent.com/114147352/230919135-14385767-ffb8-4058-bc1c-b5bbcb1b8ec3.jpg">
<h3>
2. <a href="https://github.com/xhdixhfl/Goggles_project/blob/main/model/model_save.py">model_save</a>
</h3>
→ 실행 초반에 모델을 불러오는데 시간이 소요됨 또한, 임베딩 층과 문장 코퍼스를 나누는데 시간 소요가 발생함(약 15분 가량) <br>
→ 시간 소요를 단축하고자 tar파일로 모델, 임베딩층, 코퍼스 등을 저장하는 코드
<h3>
3. <a href="https://github.com/xhdixhfl/Goggles_project/blob/main/model/KST_model.py">KST_model</a>
</h3>
→ 최종 장고에 저장된 파일 형식<br>
→ 2에서 저장된 tar파일을 불러옴으로서 초기 로딩 시간을 단축시킴(약 10분 정도)
