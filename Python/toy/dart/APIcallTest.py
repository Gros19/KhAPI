from  urllib.request import urlopen
import xml.etree.ElementTree as ET
import zipfile
import io
import os, sys
import pandas as pd
import tool.API_KEY
from tool.utils import get_project_root

# 모든 행과 열을 출력합니다.
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 출력되는 행과 열의 수를 제한합니다.
# pd.options.display.max_rows = 60
# pd.options.display.max_columns = 20

# c:\KhAPI\Python\toy\data\dart\corpcode  
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# C:\KhAPI\data\dart\corpcode\CORPCODE.xml

# CORPCODE.xml 파일을 저장할 경로
saveXmlDir = f"{get_project_root()}\\data\\dart\\corpcode"
print(" CORPCODE.xml 저장 경로: ", saveXmlDir)

# API_KEY = "발급한 API 키를 입력하세요"
API_KEY = tool.API_KEY

class DartReq:
    def __init__(self,dart_api_key):
        self.api_key = dart_api_key
        
    # CORPCODE.xml을 다운로드 합니다.
    def down_corp_codeXML(self, saveXmlDir):
        url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key="
        with urlopen(url+self.api_key) as zipresp:
            with io.BytesIO(zipresp.read()) as ioB:
                with zipfile.ZipFile(ioB) as zip:
                    zip.extractall(saveXmlDir)
                    
    # xml파일을 파싱한 결과를 반환합니다.
    def parse_corp_code(self, saveXmlDir):
        corp_code = []
        stock_code = []
        corp_name = []

        #다운받은 xml파일을 불러옵니다.
        xml_file = f"{saveXmlDir}\CORPCODE.xml"
        print(" parse_corp_code",xml_file)
        doc = ET.parse(xml_file).getroot()
        list_tg = doc.findall("list")

        # corp_code, stock_code, corp_name 각 배열에 항목을 추가합니다.
        for i in list_tg:
            corp_code.append(i.find("corp_code").text)
            corp_name.append(i.find("corp_name").text)

            # stock_code가 빈 항목이 존재하기 때문에 임의로 지정했습니다.
            if i.find("stock_code").text == " ":
                stock_code.append("99999999")
            else:
                stock_code.append(i.find("stock_code").text)

        res = {"corp_code": corp_code, "stock_code": stock_code, "corp_name": corp_name}
        return res  



doDar = DartReq(API_KEY.key)
# corp_code 파일을 다운로드 받습니다.
# doDar.down_corp_codeXML(saveXmlDir)


# parse_corp_code 함수 호출
corp_info = doDar.parse_corp_code(saveXmlDir)

p1 = pd.DataFrame(corp_info)

# 마지막 번호 999980	99999999	금감원(테스트)
p1 = p1.set_index('stock_code').sort_index()
print(p1.loc[:"99980"][:10])

print((200**221)%611)
