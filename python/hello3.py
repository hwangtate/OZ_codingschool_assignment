from hello2 import BungeoppangShop

def main():
    shop = BungeoppangShop(
        stock ={
            "팥붕어빵": 10,
            "슈크림붕어빵": 8,
            "초코붕어빵": 5
        },
        price ={
            "팥붕어빵": 1000,
            "슈크림붕어빵": 1200,
            "초코붕어빵": 1500
        },
        sales = {
            "팥붕어빵": 0,
            "슈크림붕어빵": 0,
            "초코붕어빵": 0
        }
    )

    while True:
        mode = input("모드를 선택해주세요. 1.주문 모드 2. 관리자 모드")
        if mode == "1":
            shop.process_order()
        elif mode == "2":
            shop.admin_mode()
        elif mode == "종료":
            shop.calculate_total_sales()
            print("프로그램을 종료합니다.")
            break
        else:
            print("1 또는 2를 입력해주세요.(혹은 종료)")
        

main()