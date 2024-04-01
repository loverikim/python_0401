import re

word = "한글과 english"
reg = re.compile(r'[가-힣]]')

if reg.match(word):
    print("한글입니다.")

