# [streamlit_prototype](https://seokjam-prototype-streamlit-main-wjiy15.streamlit.app/) 
> streamlit으로 배포한 streamlit 프로토타입 교안(https://seokjam-prototype-streamlit-main-wjiy15.streamlit.app/)

## 💻 Streamlit 프로토타입 만들기

### 1. [Streamlit](https://streamlit.io/)이란?

***'A faster way to build and share data apps'***
Streamlit 은 데이터 프로토타이핑 (Data Prototyping) 도구입니다.
간단한 기능을 가진 데이터 웹 어플리케이션을,
빠르고 간단하게 눈으로 확인할 수 있는 웹 형태로 만들 수 있다는 것이 가장 큰 장점입니다.

**[장점]**
> - Python 환경이기에 초보자도 쉽게 사용할 수 있습니다.
> - Streamlit 패키지 설치 후 적절한 함수만 호출하면 사용할 수 있습니다.
> - Script를 업데이트 할 때 마다 변경사항을 바로 확인 가능합니다.
---

### 2. Streamlit 시작하기
#### ① PyCharm(파이참) 실행 및 프로젝트 생성하기
![0-1.Create Project](https://github.com/seokjam/streamlit_prototype/blob/master/image/0-1.Create%20Project.jpg)
Pycharm을 실행하고 'New Project' 버튼을 클릭합니다.

![0-2.Conda Env Project Create](https://github.com/seokjam/streamlit_prototype/blob/master/image/0-2.Conda%20Env%20Project%20Create.jpg)
**'Location'** 에 신규 프로젝트 생성 디렉토리를 입력하고,
'Python Interpreter를 New environment using을 Conda로 설정한 뒤 **'Create'** 를 클릭합니다.
---

#### ② Streamlit 설치하기 
  Terminal(터미널) 창을 열고 다음 명령어를 실행합니다.
  
  ```
  pip install streamlit
  ```
---

#### ③ Streamlit 실행하기
  **'Main.py'** 라는 파이썬 파일을 하나 만들고, 아래의 코드를 복사하여 붙여넣고 저장합니다.
  ```
  import streamlit as st
  
  st.set_page_config(
    page_title='Streamlit 프로토타입 만들기'
    page_icon='🎈',
    layout='wide'
  )
  
  st.text('🎈Streamlit 프로토타입 만들기')
  ```          

터미널 창에서 다음 명령어를 실행합니다.
  ```
  streamlit run Main.py
  ```
---

**'http://localhost:8501/'** 주소로 다음과 같은 페이지가 출력되는지 확인합니다.
![0-3.Run Streamlit](https://github.com/seokjam/streamlit_prototype/blob/master/image/0-3.Run%20Streamlit.jpg)
---
## 축하 드립니다.🎉🎉🎉
#### 이제 여러분은 나만의 웹 페이지를 만드셨습니다.
#### Streamlit의 기본 기능들은 왼쪽 메뉴에서 살펴 볼 수 있습니다.
