class BungeoppangShop:
    def __init__(self,stock,price,sales):
        self.stock = stock
        self.price = price
        self.sales = sales
        self.order_list ={}

    def check_stock(self):
        now_stock = print(f"현재 재고 : {self.stock}")
        return(now_stock)
    
    def process_order(self):
        print("<주문 모드>")
        while True:
            self.bread_type = input("주문하실 붕어빵 종류를 입력해주세요 :")
            if self.bread_type == "종료":
                break
            elif self.bread_type not in self.stock:
                print("잘못된 값을 입력했습니다. 모드를 종료합니다.")
                break

            self.bread_count = input("주문하실 붕어빵 개수를 입력해주세요 :")
            if self.bread_count == "종료":
                break
            
            try:
                self.bread_count = int(self.bread_count)       
            except ValueError:
                print("잘못된 값을 입력하셨습니다. 모드를 종료합니다.")
                break
            
            self.order_list[self.bread_type] = self.bread_count # :)

            if self.stock[self.bread_type] >= int(self.order_list[self.bread_type]):
                self.stock[self.bread_type] -= int(self.order_list[self.bread_type])
            elif self.stock[self.bread_type] < int(self.order_list[self.bread_type]):
                print("재고가 부족합니다. 모드를 종료합니다.")
                break
            print("=" * 50)
            print(f"주문하신 내용은 : {self.order_list}입니다.")
            print(f"현재 재고는 : {self.stock}입니다.")
            print("=" * 50)
        
    def admin_mode(self):
        print("<관리자 모드>")
        while True:
            
            self.bread_type = input("추가할 붕어빵 종류를 입력해주세요 :")
            if self.bread_type == "종료":
                break
            elif self.bread_type not in self.stock:
                print("잘못된 값을 입력했습니다. 모드를 종료합니다.")
                break

            self.bread_count = input("추가할 붕어빵 개수를 입력해주세요 :")
            if self.bread_count == "종료":
                break
            
            try:
                self.bread_count = int(self.bread_count)       
            except ValueError:
                print("잘못된 값을 입력했습니다. 모드를 종료합니다.")
                break

            stock_list = {
                self.bread_type : self.bread_count 
            }
            print("=" * 50)
            print(f"추가하신 재고  : {stock_list}")
            print("=" * 50)
            
            self.stock[self.bread_type] += int(stock_list[self.bread_type])
            
            print(self.stock)
    def calculate_total_sales(self): 
        
        sales_count = {
            "팥붕어빵": 0,
            "슈크림붕어빵": 0,
            "초코붕어빵": 0
        }

        sales_ = {
            "팥붕어빵": 0,
            "슈크림붕어빵": 0,
            "초코붕어빵": 0
        }

        for key in self.order_list:
            sales_count[key] += int(self.order_list[key]) 
        print("=" * 50)
        print(f"주문내역 : {self.order_list} \n")

        total_sales = 0

        for j in sales_:
            sales_[j] = self.price[j] * sales_count[j]

            total_sales += sales_[j]


        print(f"매출 : {sales_}원 \n") 
        print(f"총매출 : {total_sales}원")
        print("=" * 50)            
