from eh import Bankaccount
from eh import Start

a=[]
num=0
st = Start(a,num)

number = 0    #프로그램 종료 변수 
while number!=5 :
    print("======Bank Menu=====")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 프로그램 종료")
    print("====================")
    n = input("입력: ")
    if n=='1':
       st.one(a,num)
    elif n=='2':
        st.two(a, num)
    elif n=='3' :
        st.three(a, num)
    elif n=='4' :
        st.four(a, num)
    elif n=='5' : 
        number = 5
    else:
        print("\n**잘못 입력하셨습니다**\n")
        