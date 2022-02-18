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



# CFS:연결재무제표, OFS:재무제표
fs_div = "CFS"
crtfc_key = API_KEY.key
corp_code = "00126380"

# 1분기보고서 : 11013
# 반기보고서 : 11012
# 3분기보고서 : 11014
# 사업보고서 : 11011
reprt_code = [11013, 11012, 11014, 11011]
# 2015년도 이후부터 제공
bsns_year = 2016



cash_flow_pd = pd.DataFrame()
balance_sheet_pd = pd.DataFrame()
income_statement_pd = pd.DataFrame()




for bsns_year in  range(2015,2023):
    for quarter in [0, 1, 2]:
        if quarter == 2 or quarter == 0:
            continue

        def okCheck(num):
            message = {"000":"정상", "010":"등록되지 않은 키입니다.", 
             "011":"사용할 수 없는 키입니다. 오픈API에 등록되었으나, 일시적으로 사용 중지된 키를 통하여 검색하는 경우 발생합니다.", 
             "012":"접근할 수 없는 IP입니다.", "013":"조회된 데이타가 없습니다.", 
             "014":"파일이 존재하지 않습니다.", "020":"요청 제한을 초과하였습니다.\n일반적으로는 10,000건 이상의 요청에 대하여 이 에러 메시지가 발생되나, 요청 제한이 다르게 설정된 경우에는 이에 준하여 발생됩니다.", 
             "100":"필드의 부적절한 값입니다. 필드 설명에 없는 값을 사용한 경우에 발생하는 메시지입니다.", "":"", 
             "101":"부적절한 접근입니다.", "800":"시스템 점검으로 인한 서비스가 중지 중입니다.", 
             "900":"정의되지 않은 오류가 발생하였습니다.", "901":"사용자 계정의 개인정보 보유기간이 만료되어 사용할 수 없는 키입니다. 관리자 이메일(opendart@fss.or.kr)로 문의하시기 바랍니다."}
            if num == "000":
                return 1
            print(message[num])
            return None


        def cashFlowFilter(name):
            word_dic= ["영업활동현금흐름",
                       "영업에서창출된현금흐름",
                       "영업에서창출된현금흐름",
                       "당기순이익",
                       "조정",
                      "영업활동으로인한자산부채의변동",
                       "이자의수취",
                       "이자의지급",
                       "배당금수입",
                       "법인세납부액",
                       
                       "투자활동현금흐름",
                       
                       "재무활동현금흐름",
                       
                       "현금및현금성자산의순증감",
                       "기초의현금및현금성자산",
                       "기말의현금및현금성자산"]
            return name in word_dic
        
        def balanceSheetFilter(name):
            word_dic = ["유동자산" ,
                        "현금및현금성자산" ,
                        "매출채권" ,
                        "미수금" ,
                        "선급비용" ,
                        "재고자산" ,
                        "비유동자산" ,
                        "유형자산" ,
                        "무형자산" ,
                        "이연법인세자산" ,
                        "유동부채" ,
                        "매입채무" ,
                        "단기차입금" ,
                        "미지급금" ,
                        "선수금" ,
                        "예수금" ,
                        "미지급비용" ,
                        "당기법인세부채" ,
                        "유동성장기부채" ,
                        "충당부채" ,
                        "기타유동부채" ,
                        "매각예정분류부채" ,
                        "비유동부채" ,
                        "사채" ,
                        "장기차입금" ,
                        "장기미지급금" ,
                        "순확정급여부채" ,
                        "이연법인세부채" ,
                        "장기충당부채" ,
                        "기타비유동부채" ,
                        "부채총계" ,
                        "지배기업소유주지분" ,
                        "자본금" ,
                        "우선주자본금" ,
                        "보통주자본금" ,
                        "주식발행초과금" ,
                        "이익잉여금" ,
                        "기타자본항목" ,
                        "매각예정분류기타자본항목" ,
                        "비지배지분" ,
                        "자본총계" ,
                        "부채와자본총계"]
            return name in word_dic


        def reword(brbr):
            word_dic = {
                "현금및현금성자산의순증가":"현금및현금성자산의순증감",
                "현금및현금성자산의증가":"현금및현금성자산의순증감",
                "기초현금및현금성자산":"기초의현금및현금성자산",
                "기말현금및현금성자산":"기말의현금및현금성자산",
                "자본과부채총계":"부채와자본총계"
            }
            if brbr in word_dic.keys():
                return word_dic[brbr]
            else:
                return brbr

        # 단일회사 전체 재무제표 개발가이드
        url = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.xml"

        reqStr = f"{url}?crtfc_key={crtfc_key}&corp_code={corp_code}&reprt_code={reprt_code[quarter]}&bsns_year={bsns_year}&fs_div={fs_div}"
        print(bsns_year, reqStr,end="\n")

        with urlopen(reqStr) as respon:
            doc = ET.parse(respon).getroot()
            if 1 == okCheck(doc.find("status").text):

                # 현금흐름표 계정명
                account_nm_cash = []
                # 당기금액           
                thstrm_amount_cash = []
                
                # 재무상태표 계정명
                account_nm_balance = []
                # 당기금액           
                thstrm_amount_balance = []
                
                # 손익계산서 계정명
                account_nm_income = []
                # 당기금액           
                thstrm_amount_income = []

                # 응답 결과 중에서 파싱
                list_tg = doc.findall("list")
                
                # 이번 분기
                # 해당 보고서가 몇기인지
                thstrm_nm= list_tg[0].find("thstrm_nm").text


                for element in list_tg:

                    if element.find("sj_nm").text == "현금흐름표":
                        
                        am_name = element.find("account_nm").text
                        am_name = am_name.replace(" ", "")
                            


                        if am_name.find("(") > -1:
                            left = am_name.find("(")
                            am_name = am_name[:left]
                            
                        am_name = reword(am_name)

                        if cashFlowFilter(am_name) == True:
                            account_nm_cash.append(am_name)
                            thstrm_amount_cash.append(element.find("thstrm_amount").text)
                    
                    elif element.find("sj_nm").text == "재무상태표":
                        am_name = element.find("account_nm").text
                        am_name = am_name.replace(" ", "")
                        
                        if am_name.find("(") > -1:
                            left = am_name.find("(")
                            am_name = am_name[:left]
                        am_name = reword(am_name)
                        
                        if balanceSheetFilter(am_name) == True:
                            account_nm_balance.append(am_name)
                            thstrm_amount_balance.append(element.find("thstrm_amount").text)
                    
                    
                    elif element.find("sj_nm").text == "손익계산서":
                        am_name = element.find("account_nm").text
                        am_name = am_name.replace(" ", "")
                        
                        if am_name.find("(") > -1:
                            left = am_name.find("(")
                            am_name = am_name[:left]
                        am_name = reword(am_name)
                        account_nm_income.append(am_name)
                        thstrm_amount_income.append(element.find("thstrm_amount").text)




                cash_flow_thstrmpd = pd.DataFrame({thstrm_nm:thstrm_amount_cash}, index=account_nm_cash) 
                
                balance_sheet_thstrmpd = pd.DataFrame({thstrm_nm:thstrm_amount_balance}, index=account_nm_balance) 
                
                income_state_thstrmpd = pd.DataFrame({thstrm_nm:thstrm_amount_income}, index=account_nm_income) 
                print(thstrm_nm, "*"*100 ,sep='\n',end ="\n\n")

                cash_flow_pd = pd.concat([cash_flow_pd,cash_flow_thstrmpd], axis=1)
                
                balance_sheet_pd = pd.concat([balance_sheet_pd, balance_sheet_thstrmpd], axis=1)    
                
                income_statement_pd = pd.concat([income_statement_pd, income_state_thstrmpd], axis=1)
                
                balance_sheet_pd = balance_sheet_pd.reindex(index=
                                                            ["유동자산" ,
                                                            "현금및현금성자산" ,
                                                            "매출채권" ,
                                                            "미수금" ,
                                                            "선급비용" ,
                                                            "재고자산" ,
                                                            "비유동자산" ,
                                                            "유형자산" ,
                                                            "무형자산" ,
                                                            "이연법인세자산" ,
                                                            "유동부채" ,
                                                            "매입채무" ,
                                                            "단기차입금" ,
                                                            "미지급금" ,
                                                            "선수금" ,
                                                            "예수금" ,
                                                            "미지급비용" ,
                                                            "당기법인세부채" ,
                                                            "유동성장기부채" ,
                                                            "충당부채" ,
                                                            "기타유동부채" ,
                                                            "매각예정분류부채" ,
                                                            "비유동부채" ,
                                                            "사채" ,
                                                            "장기차입금" ,
                                                            "장기미지급금" ,
                                                            "순확정급여부채" ,
                                                            "이연법인세부채" ,
                                                            "장기충당부채" ,
                                                            "기타비유동부채" ,
                                                            "부채총계" ,
                                                            "지배기업소유주지분" ,
                                                            "자본금" ,
                                                            "우선주자본금" ,
                                                            "보통주자본금" ,
                                                            "주식발행초과금" ,
                                                            "이익잉여금" ,
                                                            "기타자본항목" ,
                                                            "매각예정분류기타자본항목" ,
                                                            "비지배지분" ,
                                                            "자본총계" ,
                                                            "부채와자본총계"])
            else:
                continue

    
# print(balance_sheet_pd.fillna(0))
dodart = DartReq(API_KEY)


p1 = pd.DataFrame(dodart.parse_corp_code(saveXmlDir))
p1 = p1.set_index('stock_code').sort_index()


# print(p1.loc[:"99980"][:50])

print(API_KEY.key)