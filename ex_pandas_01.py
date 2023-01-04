# ------------------------------------------------------------
# 연산 실습
# ------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------
import pandas as pd

FILE=r'datafiles\stock price.xlsx'

# [1] 주식 id, 회사 이름, 가격만 사용 ===========================
stockDF=pd.read_excel(FILE)

# 데이터 확인 => info() or head() or tail() or describe()
stockDF.info()
NstockDF=stockDF[['id','stock_name','price']]

# 데이터 파일 읽어 들일 때 설정할 수도 있음------------------------
# 로딩할 특정 컬럼 지정 => usecols='엑셀에서의 columns 인덱스'
stockDF2=pd.read_excel(FILE,usecols='A:B,D')
print(stockDF2)
# --------------------------------------------------------------


# [2] 가격에 대한 *100 결과 추가 ==================================
NstockDF['price100']=NstockDF['price']*100 # =NstockDF.price * 100  or =NstockDF.prce.mul(100,fill_value=0)
print(NstockDF)


# [3] id col을 idx로 설정 ========================================
NstockDF.set_index('id',inplace=True)
print(NstockDF)

# 데이터 파일 읽어 들일 때 설정할 수도 있음 => 매개변수(파라미터) index_col
# 특정 컬럼 인덱스로 설정 => index_col 매개변수
stockDF=pd.read_excel(FILE,index_col=0)
print(stockDF)
# ================================================================
print()
stockDF3=pd.read_excel(FILE,usecols='A:C',index_col=0,skipfooter=3,skiprows=3)
# skiprows 하면 컬럼 이름 날아가버리는데 lambda함수 써서 살리는 방법 있음 skiprows의 api설명-----------------
# Line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file.
# If callable, the callable function will be evaluated against the row indices, returning True
# if the row should be skipped and False otherwise. An example of a valid callable argument
# would be lambda x: x in [0, 2].
# ------------------------------------------------------------------------------------------------------
print(stockDF3)


# parse-dates[] => 컬럼명 지정하면 해당 컬럼의 타입이 datetime64로 변경
# dayfirst => ddmm(일월) 순서로 설정 False 디폴트값
# infer_datetime_format[] => 날짜 시간 포맷을 추정해서 파싱
# date_parser[] => 직접 날짜 시간 포맷 설정 function
# from datetime import datetime #날짜시간관련 모듈 # 다른방법2
FILE2=r'datafiles\banklist.csv'
# _date_parser=lambda x : datetime.strptime(x,'%d-%b') # 다른방법2
# bankDF=pd.read_csv(FILE2,parse_dates=['Updated Date'],date_parser=_date_parser) # 다른방법2
bankDF=pd.read_csv(FILE2,parse_dates=['Updated Date','Closing Date'],dayfirst=False,infer_datetime_format=True) #방법1
bankDF.info()
print(bankDF.head(3))