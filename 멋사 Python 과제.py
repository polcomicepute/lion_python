
class Bankaccount: #계좌 class 선언
    name = "익명인"
    account = 1
    money = 0
    def __init__(self, name, account, money):
        self.account = account
        self.name = name
        self.money = money
        print("##계좌개설을 완료하였습니다##")
    def in_money(self, name, account):
        if((self.name == name)&(self.account == account)): #계좌랑 이름 일치하는지 확인
             print("계좌잔고: %d 원"%(self.money))
             add = int(input("입금하실 금액을 입력해주세요 : "))
             if(add <0):
                 print("**잘못 입력하셨습니다**")
                 return 0
             self.money += int(add)
             print("##계좌잔고: ",self.money,"원##")
             print("##입금이 완료되었습니다##")
        else:
            print("**잘못 입력하셨습니다**")
    def out_money(self, name, account):
        if((self.name == name)&(self.account == account)):  #계좌랑 이름 일치하는지 확인
             print("계좌잔고: %d 원"%(self.money))
             sub = int(input("출금하실 금액을 입력해주세요 : "))
             if (sub > self.money):
                 print("##잔고가 부족하여 출금에 실패하였습니다##")
                 return 0
             if(sub<0):
                 print("**잘못 입력하셨습니다**")
                 return 0
             self.money -= int(sub)
             print("##계좌잔고: ",self.money,"원##")
             print("##출금이 완료되었습니다##")
        else:
            print("**잘못 입력하셨습니다**")
    def list_account(self): #계좌 출력
        print("계좌번호: %s / 이름: %s / 잔액: %d 원"%(self.account, self.name, self.money))

a = []
number = 0    #프로그램 종료 변수     
num = 0; #계좌 총 개수
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
        print("\n======계좌개설======")
        account = input("계좌번호: ")
        name = input("이름: ")
        money = int(input("예금: "))
        if (money>=0):
            a.insert(num,Bankaccount(name, account, money))
            num = num + 1 #계좌 총 개수 증가!
        else:
            print("**잘못 입력하셨습니다**")
        print("====================\n")
    elif n=='2':
        ac = -1
        print("\n======입금하기======")
        account = input("입금하실 계좌 번호를 입력해주세요: ")
        name = input("계좌이름: ")
        for i in range(0,num):#계좌 번호와 일치하는 class변수 찾기
            if(a[i].account==account):
                ac = i
        if(ac == -1):#일치하는 계좌가 없는 경우
            print("**잘못 입력하셨습니다**1")
        else: #일치하는 계좌가 있는 경우
            a[i].in_money(name, account)
        print("====================\n")
    elif n=='3' :
        ac = -1
        print("\n======출금하기======")
        account = input("출금하실 계좌 번호를 입력해주세요: ")
        name = input("계좌이름: ")
        for i in range(0,num): #계좌 번호와 일치하는 class변수 찾기
            if(a[i].account==account):
                ac = i
        if(ac == -1):  #일치하는 계좌가 없는 경우
            print("**잘못 입력하셨습니다**")
        else: #일치하는 계좌가 있는 경우
            a[i].out_money(name, account)
        print("====================\n")
    elif n=='4' :
        print("\n======전체조회======")
        for i in range(0,num):#모든 계좌들 출력
            a[i].list_account()
        print("====================\n")
    elif n=='5' : 
        number = 5
    else:
        print("\n**잘못 입력하셨습니다**\n")
