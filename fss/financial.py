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
print(fs['is']["[D310000] Income statement, by function of expense - Consolidated financial statements (Unit: KRW)"]["label_ko"])


# from flask import Flask  #서버 구현을 위한 Flask 객체 import
# from flask_restx import Api, Resource #Api 구현을 위한 Api 객체 import
#
# app = Flask(__name__) #Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌
# api = Api(app) #Flask 객체에 Api 객체 등록
#
# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return fs['cf']
# if __name__=="__main__":
#     app.run()