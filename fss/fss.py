import json
import dart_fss as dart
#KEY.json에서 API KEY 불러오기
with open("KEY.json", "r") as f:
    json_data = json.load(f)
    
key1 = json_data["key"]
key2 = json_data["key2"]


#api key 설정
dart.set_api_key(api_key=key1)
print("api :",dart.get_api_key)
# 삼성전자 code 
# corp_code = '00126380'   
##
# sk code
corp_code = '00181712'
result = dart.api.info.stock_totqy_sttus(corp_code=corp_code, bsns_year="2020", reprt_code="11013")

for a in result["list"]:
    print( a["istc_totqy"])

