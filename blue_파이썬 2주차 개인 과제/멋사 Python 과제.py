from eh import Bankaccount
from eh import Start

st = Start()
while 1 :
    print("======Bank Menu=====")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 계좌이체")
    print("6. 프로그램 종료")
    print("====================")
    n = input("입력: ")
    if n=='1':
       st.one()
    elif n=='2':
        st.two()
    elif n=='3' :
        st.three()
    elif n=='4' :
        st.four()
    elif n=='5' :
        st.five()
    elif n=='6' : 
        break
    else:
        print("\n**잘못 입력하셨습니다**\n")
        
