# 환율 구하기 -> forex-python 라이브러리 활용.

from forex_python.converter import CurrencyRates

rate = CurrencyRates()

krw_rate = rate.get_rate("USD", "KRW")
print(krw_rate)