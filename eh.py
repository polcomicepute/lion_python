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
             isnum=input("입금하실 금액을 입력해주세요 : ")
             if isnum.isdecimal():
                add = int(isnum)
                if(add <0):
                     print("**잘못 입력하셨습니다**")
                     return 0
                self.money += int(add)
                print("##계좌잔고: ",self.money,"원##")
                print("##입금이 완료되었습니다##")
             else:
                print("**잘못 입력하셨습니다. 숫자로 입력해주세요^^**")
                return 0
        else:
            print("**잘못 입력하셨습니다**")
    def out_money(self, name, account):
        if((self.name == name)&(self.account == account)):  #계좌랑 이름 일치하는지 확인
             print("계좌잔고: %d 원"%(self.money))
             isnum=input("출금하실 금액을 입력해주세요 : ")
             if isnum.isdecimal():
                sub = int(isnum)
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
                print("**잘못 입력하셨습니다. 숫자로 입력해주세요^^**")
                return 0
        else:
            print("**잘못 입력하셨습니다**")
    def list_account(self): #계좌 출력
        print("계좌번호: %s / 이름: %s / 잔액: %d 원"%(self.account, self.name, self.money))

class Start:
    a = []
    num = 0
    def __init__(self):
        self.a=[]
        self.num=0
   
      #계좌 총 개수
    def one(self):
        print("\n======계좌개설======")
        account = input("계좌번호: ")
        if account.isdecimal():
            name = input("이름: ")
            isnum=input("예금: ")
            if isnum.isdecimal():
                money = int(isnum)
                if (money>=0):
                    self.a.insert(self.num,Bankaccount(name, account, money))
                    self.num= self.num+ 1
                    #s=num+1
                    # #계좌 총 개수 증가!
                else:
                    print("**잘못 입력하셨습니다**")
            else:
                print("**잘못 입력하셨습니다**")
        else:
            print("**잘못 입력하셨습니다**")
        
        print("====================\n")
    def two(self):
        ac = -1
        print("\n======입금하기======")
        account = input("입금하실 계좌 번호를 입력해주세요: ")
        name = input("계좌이름: ")
        for i in range(0,self.num):#계좌 번호와 일치하는 class변수 찾기
            if(self.a[i].account==account):
                ac = i
        if(ac == -1):#일치하는 계좌가 없는 경우
            print("**잘못 입력하셨습니다**")
        else: #일치하는 계좌가 있는 경우
            self.a[ac].in_money(name, account)
        print("====================\n")
    def three(self):
        ac = -1
        print("\n======출금하기======")
        account = input("출금하실 계좌 번호를 입력해주세요: ")
        name = input("계좌이름: ")
        for i in range(0,self.num): #계좌 번호와 일치하는 class변수 찾기
            if(self.a[i].account==account):
                ac = i
        if(ac == -1):  #일치하는 계좌가 없는 경우
            print("**잘못 입력하셨습니다**")
        else: #일치하는 계좌가 있는 경우
            self.a[ac].out_money(name, account)
        print("====================\n")
    def four(self):
        print("\n======전체조회======")
        for i in range(0,self.num):#모든 계좌들 출력
            self.a[i].list_account()
        print("====================\n")

        

