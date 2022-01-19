from  urllib.request import urlopen
import xml.etree.ElementTree as ET
import zipfile
import io
import os, sys
import pandas as pd
import tool.API_KEY
from tool.utils import get_project_root

print(sys.path)
# 한번이라면 
# CORPCODE.xml 저장 경로: 
# c:\KhAPI\Python\toy\data\dart\corpcode  
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))



# CORPCODE.xml 파일을 저장할 경로, 프로젝트 최상위에 data폴더로 설정한다
saveFileDir = f"{get_project_root()}\\data\\dart\\corpcode"
print(" CORPCODE.xml 저장 경로: \n", saveFileDir)

saveFileDir = "c:\KhAPI\data\dart\corpcode";
API_KEY = "발급한 API 키를 입력하세요"
API_KEY = tool.API_KEY

# CORPCODE.xml을 다운로드 합니다.
def down_corp_codeXML(API_KEY, saveFileDir):
    url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key="
    with urlopen(url+API_KEY) as zipresp:
        with io.BytesIO(zipresp.read()) as ioB:
            with zipfile.ZipFile(ioB) as zip:
                zip.extractall(saveFileDir)
                
    
# xml파일을 파싱한 결과를 list 형태로 리턴합니다.
def parse_corp_code(saveFileDir):
    # 아래는 파일 결과 예시:
    """
    <result>
        <list>
            <corp_code>00434003</corp_code>
            <corp_name>다코</corp_name>
            <stock_code> </stock_code>
            <modify_date>20170630</modify_date>
        </list>
        <list>
            <corp_code>00434456</corp_code>
            <corp_name>일산약품</corp_name>
            <stock_code> </stock_code>
            <modify_date>20170630</modify_date>
        </list>
        <list>
            <corp_code>00430964</corp_code>
            <corp_name>굿앤엘에스</corp_name>
            <stock_code> </stock_code>
            <modify_date>20170630</modify_date>
        </list>
    </result>
    """
    
    corp_code = []
    stock_code = []
    corp_name = []
    
    #다운받은 xml파일을 불러옵니다.
    xml_file = f"{saveFileDir}\CORPCODE.xml"
    print(xml_file)
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
            
    res = [corp_code, stock_code, corp_name]
    return res  



# parse_corp_code 함수 호출
pars_res = parse_corp_code(saveFileDir)

corp_info = {"corp_code": pars_res[0], "stock_code":pars_res[1], "corp_name":pars_res[2]}

p1 = pd.DataFrame(corp_info)

print(p1['stock_code'].tail())
