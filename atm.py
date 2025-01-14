# 기본 금액 : balance (변수명)
# 기본 금액 변수에 3000원을 넣어주세요 -> 값을 넣어주세요
# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 계속해서 노출되도록 만들어주세요.
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요

#입금한 금액을 받는 변수 : deposit_amount
#입금된 금액은 balance 변수에 추가되도록 코드를 작성해주세요.
#영수증에 다음 순서로 값이 들어가도록 코드를 만들어 주세요. - > '입금', 입금 요청액, 총액 순으로 데이터 넣어주세요.
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
#영수증 변수는 : receipts
'''
'''
#출금한 금액을 받는 변수 : withdraw_amount
#출금을 요청한 금액은 balance 변수에 뺀 결과가 들어가도록 코드를 작성해주세요.
#영수증에 다음 순서로 값이 들어가도록 코드를 만들어 주세요. - > "출금", withdraw_amount, balance) 순으로 데이터 넣어주세요.
#가지고 있는 금액보다 출금을 원하는 금액 클때 가지고 있는 금액만 출금되도록 코드를 작성해주세요.
#단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
#영수증 변수는 : receipts


#입력 검증 및 에러 처리 추가
#잘못된 입력 값(숫자가 아닌값, 음수 값 등)을 처리하도록 기능을 추가해주세요
#유효하지 않은 메뉴 선택 시 경고 메시지 또는 사용방법 재안내를 해주세요.

balance = 3000
receipts = []

while True:
    num = input("사용하실 기능을 선택해주세요. (1: 입금, 2: 출금, 3: 영수증 보기, 4: 종료)")
    if num == '4':
        break
    if num == '1':
        deposit_amount = input("입금할 금액을 입력해주세요 : ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount) # balance = balance + deposit_amount
            receipts.append(("입금", deposit_amount, balance))
            print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.\n')
        else:
            print("입금한 금액을 숫자 형태와 음수가 아닌값을 입력해주세요")

    if num == '2':
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : "))
        withdraw_amount = min(withdraw_amount, balance)
        balance -= withdraw_amount # balance = balance - withdraw_amount
        receipts.append(("출금", withdraw_amount, balance))
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.\n')    

    if num == '3':
        #영수증 값이 있을때, 값이 없을때
        if receipts: # 프로그램이 시작되자마자 3번을 눌렀을 경우 이 조건은 참? 거짓? 거짓
            print("=== 영수증 내역 ===")
            for i in receipts:
                print(f'{i[0]} : {i[1]}원 | 잔액은 {i[2]}원 입니다.')
            print("=================\n")
        else:
            print("영수증 내역이 없습니다.")


print(f'서비스를 종료합니다. \n현재 잔액: {balance}')