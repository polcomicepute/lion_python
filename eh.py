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