# Goggles project
> 22년도 3차 차세대 빅데이터 기반 크리에이터 양성과정 훈련 최종프로젝트<br>
> 기간 : 22.12.16. ~ 23.02.15.
<br>

## 프로젝트 소개

- **주제** : 시각 장애인을 대상으로 제품(매장)에 대한 정보 접근성을 향상 시키기위한 서비스 제공
- **기획배경** : 오프라인 매장에서 제품 정보를 얻기 어려운 디지털 사회 약자의 접근성을 높일 수 있는 방안이 필요함
- **기획목적** <br>
  - 23년 개정 시행될 장애인 차별금지 및 권리 구제 등에 관한 법률에서 키오스크, 모바일 앱 등을 운영 배포할 때 장애인과 비장애인이 동등하게 서비스를 이용할 수 있도록 편의를 제공할 의무를 규정함<br>
  - 제도적 변화에 대응하기 위한 ESG 서비스 제안
- **핵심기능**
  - 점자 코드를 통해 상품정보를 음성(TTS)으로 제공
  - 텍스트 분류기반 유사 상품 추천 서비스
  - 이미지 OCR을 통한 제품 패키징 정보 추출 및 음성 서비스
  - 즐겨찾는 상품 등록 및 조회 페이지 제공<br>
> ☞ [전체 프로젝트 내용](https://github.com/Rudadak/FinalProject "루다닥")

## 담당 역할
1. DB구축 및 모델 훈련에 필요한 데이터 수집 <br>
☞ [웹 크롤링](https://github.com/xhdixhfl/Goggles_project/tree/main/crawling "crawling")

2. 유사도 높은 리뷰 추출 서비스 API 구현 <br>
☞ [모델](https://github.com/xhdixhfl/Goggles_project/tree/main/model "model")
+ 어플리케이션 구현    ☞ [장고](https://github.com/xhdixhfl/Goggles_project/tree/main/django "django")
