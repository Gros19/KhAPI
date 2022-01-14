from  urllib.request import urlopen
import xml.etree.ElementTree as ET
import zipfile
import io
import os, sys
#상위의 상위 폴더라서 두번 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from src.utils import get_project_root

FILENAME = ""
saveFileDir = f"{get_project_root()}\\data\\dart\\corpcode"
print("회사코드 저장 경로: ", saveFileDir)

API_KEY = "a27a4e6bf5d8701810d49839d64922a438b03918"
url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key="

with urlopen(url+API_KEY) as zipresp:
    with io.BytesIO(zipresp.read()) as ioB:
        with zipfile.ZipFile(ioB) as zip:
            FILENAME= zip.namelist()[0]
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
    <result>
    """

xml_file = f"{saveFileDir}\{FILENAME}"
print(xml_file)
doc = ET.parse(xml_file).getroot()
list_tg = doc.findall("list")

for i in list_tg:
    if i.find("stock_code").text != " ":
        print(i.find("corp_code").text, i.find("stock_code").text, i.find("corp_name").text,sep='\t')




            
            