import json
import dart_fss as dart
#KEY.json에서 API KEY 불러오기
with open("KEY.json", "r") as f:
    json_data = json.load(f)
    
key1 = json_data["key"]
key2 = json_data["key2"]

#api key 설정
dart.set_api_key(api_key=key1)
clist = dart.corp.CorpList()

for a in clist.corps:
    print(a)