from  urllib.request import urlopen
import xml.etree.ElementTree as ET
import zipfile
import io
import os, sys
import pandas as pd
#상위의 상위 폴더라서 두번 사용
#KhAPI-Python-toy/APIcallTest.py
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from src.utils import get_project_root

FILENAME = ""
saveFileDir = f"{get_project_root()}\\data\\dart\\corpcode"
print("회사코드 저장 경로: ", saveFileDir)

saveFileDir = "c:\KhAPI\data\dart\corpcode";
API_KEY = "발급한 API 키를 입력하세요"

def down_corp_codeXML(API_KEY, saveFileDir):
    url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key="
    with urlopen(url+API_KEY) as zipresp:
        with io.BytesIO(zipresp.read()) as ioB:
            with zipfile.ZipFile(ioB) as zip:
                zip.extractall(saveFileDir)
                
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


def parse_corp_code(saveFileDir):
    a = []
    b = []
    c = []
    
    xml_file = f"{saveFileDir}\CORPCODE.xml"
    print(xml_file)
    doc = ET.parse(xml_file).getroot()
    list_tg = doc.findall("list")

    
    for i in list_tg:
        # if i.find("stock_code").text != " ":
        #     print(i.find("stock_code").text)
        a.append(i.find("corp_code").text)
        c.append(i.find("corp_name").text)
        if i.find("stock_code").text == " ":
            b.append("99999999")
        else:
            b.append(i.find("stock_code").text)
            
    res = [a, b, c]
    return res  


abc = parse_corp_code(saveFileDir)
res = {"corp_code": abc[0], "stock_code":abc[1], "corp_name":abc[2]}

# for a in good:
#     print(a)

p1 = pd.DataFrame(res)

print(p1['stock_code'].tail())