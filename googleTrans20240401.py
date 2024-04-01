################## 환경설정 #################
import sys
import re
import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
#############################################
# 디자인한 외부 Ui파일 불러와서 저장
form_class = uic.loadUiType("ui/googleTrans.ui")[0] #인덱스 번호 꼭 써주기


class GoogleTrans(QMainWindow, form_class): #상속자
    #생성자 만들기
    def __init__(self):
        super().__init__() #부모 클래스 생성자 호출
        self.setupUi(self) #불러온 ui파일을 연결 / 두줄은 무조건 써줌.

        self.setWindowTitle("구글 한줄 번역기") #윈도우 타이틀
        self.setWindowIcon(QIcon("icon/googleIcon.png")) # 윈도우 아이콘
        self.statusBar().showMessage("Google Trans App v1.0 Made By AERI") # 윈도우 상태표시줄

        self.trans_btn.clicked.connect(self.trans_action) #signal
        self.init2_btn.clicked.connect(self.init2_action) #초기화 버튼
        self.init1_btn.clicked.connect(self.init1_action) #입력 초기화 버튼

    # 작동시킬 함수
    def trans_action(self): # 번역 실행 함수 -> slot 함수
        korText = self.kor_input.text() # kor_input에 입력된 한글 텍스트 가져오기
        # reg = re.compile(r'[^가-힣]') # 한글만 입력받는 정규표현식 ---> ^제외
        # 시작하는 단어에 따라 오류발생
        # 한글 + 숫자, 한글 + 영어 -> 번역됨
        # 숫자 + 한글, 영어 + 한글 -> 알림창
        reg = re.compile(r'[^가-힣]*$')

        # none값이기 때문에 빈공간일 때 실행을 누르면 튕김.
        # 입력이 없을 경우. pass --> 해결 안됨.
        if korText == "":
            # print("공백입력!!")

        # PyQt5 경고창 QMessageBox 경고창 띄우기
            QMessageBox.warning(self, "오류", "번역할 내용이 없습니다.\n한글 입력창에 번역할 내용을 넣어주세요.")
        elif reg.match(korText): #한글입력 여부확인(숫자 또는 영어로만 입력시 경고창 출력.)
             QMessageBox.warning(self, "입력 오류!", "한글만 입력해주세요.")
             # match가 아닌 search를 사용하는 방법으로 오류 해결해보기
        else:
            trans = googletrans.Translator() # 구글 트랜스 모듈의 객체 선언
            # print(googletrans.LANGUAGES)-> 번역 언어의 dest 약자 찾기

            engText = trans.translate(korText, dest="en") # 영어 번역 결과
            jpText = trans.translate(korText, dest="ja")  # 일어 번역 결과
            chText = trans.translate(korText, dest="zh-cn")  # 영어 번역 결과

            # https://doc.qt.io/  PyQt5 사용가능한 함수들이 나옴. Public Slot
            self.eng_input.append(engText.text)# engText는 객체라서 이상하게 출력됨.text를 붙여야 문자열로 나옴
            #번역된 영어 텍스트를 eng_input에 출력
            self.jp_input.append(jpText.text)
            self.ch_input.append(chText.text)

    def init2_action(self): #초기화 버튼 함수
        self.kor_input.clear() #입력 내용 지우기
        self.eng_input.clear()
        self.jp_input.clear()
        self.ch_input.clear()

    def init1_action(self): #입력초기화
        self.kor_input.clear()

### 아무것도 입력되지 않았을 경우, 튕김 현상(버그)이 발생. 오류가 있다.
### 프로그램을 만들었을 경우, 항상 테스트를 통해 문제가 없는지 확인하여야 함.

# 실행
if __name__=="__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())








