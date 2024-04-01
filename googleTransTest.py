import googletrans

while True:
    korStr = input("번역할 문장을 입력해주세요:")
    if korStr =="끝":
        break
    trans = googletrans.Translator()    #구글 번역 객체 생성
    result1 = trans.translate("오늘은 불타는 금요일", "en")
    # print(googletrans.LANGUAGES)-> 번역 언어의 dest 약자 찾기

    result2 = trans.translate("오늘은 불타는 금요일", "ja")
    result3 = trans.translate("오늘은 불타는 금요일", "zh-cn")
    print(f"입력하신 [{korStr}]은 영어로 [{result1.text}]입니다.") #객체로 들어오기 때문에 .text를 넣어 주어야 된다
    print(f"입력하신 [{korStr}]은 일어로 [{result2.text}]입니다.")
    print(f"입력하신 [{korStr}]은 중어로 [{result3.text}]입니다.")