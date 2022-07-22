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
print("api :",dart.get_api_key)

#상장된 모든 회사 리스트

dclass = dart.corp.CorpList(profile=False)
dclass.sectors
"""
'어로 어업',
 '여행사 및 기타 여행보조 서비스업',
 '연료 소매업',
 '연료용 가스 제조 및 배관공급업',
 '영상 및 음향기기 제조업',
 '영화, 비디오물, 방송프로그램 제작 및 배급업',
computer_sec = dclass.find_by_sector("컴퓨터 프로그래밍, 시스템 통합 및 관리업")
computer_sec = dclass.find_by_sector("자료처리, 호스팅, 포털 및 기타 인터넷 정보매개 서비스업")
computer_sec = dclass.find_by_sector("소프트웨어 개발 및 공급업")
computer_sec = dclass.find_by_sector("기초 의약물질 및 생물학적 제제 제조업")
"""
c_codes = []
c_names = []
for a in dclass.corps:
    #stock code가 있는 회사만
    if a.stock_code is not None:
        c_codes.append(a.corp_code)
        c_names.append(a.corp_name)

#len(c_codes)
#3455

corp_pd = pd.DataFrame({"corp_code":c_codes,"corp_name":c_names})
print(corp_pd)