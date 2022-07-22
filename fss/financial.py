import json
import dart_fss as dart
import pandas as pd
#KEY.json에서 API KEY 불러오기
with open("KEY.json", "r") as f:
    json_data = json.load(f)
    
key1 = json_data["key"]
key2 = json_data["key2"]

#api key 설정
dart.set_api_key(api_key=key1)


# 삼성전자 code
corp_code = '00126380'


# 2012년 01월 01일 부터 연결재무제표 검색
# fs = samsung.extract_fs(bgn_de='20120101') 와 동일
fs = dart.fs.extract(corp_code=corp_code, bgn_de='20190101')
#%%

print(fs['bs'].to_csv())