BEGIN_FUNCTION_MAP
	.Func,시간대별호가잔량추이(t1471),t1471,attr,block,headtype=A;
	BEGIN_DATA_MAP
	t1471InBlock,기본입력,input;
	begin
		종목코드,shcode,shcode,char,6;
		분구분,gubun,gubun,char,2;
		시간,time,time,char,6;
		자료개수,cnt,cnt,char,3;
	end
	t1471OutBlock,출력,output;
	begin
		시간CTS,time,time,char,6;
		현재가,price,price,long,8;
		전일대비구분,sign,sign,char,1;
		전일대비,change,change,long,8;
		등락율,diff,diff,float,6.2;
		누적거래량,volume,volume,long,12;
	end
	t1471OutBlock1,출력1,output,occurs;
	begin
		체결시간,time,time,char,6;
		메도증감,preoffercha1,preoffercha1,long,12;
		매도우선잔량,offerrem1,offerrem1,long,12;
		매도우선호가,offerho1,offerho1,long,8;
		매수우선호가,bidho1,bidho1,long,8;
		매수우선잔량,bidrem1,bidrem1,long,12;
		매수증감,prebidcha1,prebidcha1,long,12;
		총매도,totofferrem,totofferrem,long,12;
		총매수,totbidrem,totbidrem,long,12;
		순매수,totsun,totsun,long,12;
		매수비율,msrate,msrate,float,6.2;
		종가,close,close,long,8;
	end
	END_DATA_MAP
END_FUNCTION_MAP

t1471