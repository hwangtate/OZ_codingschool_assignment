class Transaction:
    def __init__(self, transaction_type : str, amount : int, balance : int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.__balance = balance

    #문자열 반환 메서드
    def __str__(self) -> str:
        return f"거래 타입 : {self.transaction_type}\n거래 금액 : {self.amount}\n거래 후 잔고 : {self.__balance}"
    
    #튜플 변환 메서드
    def to_tuple(self) -> tuple:
        self.transaction_type = (self.transaction_type,)
        self.amount =  (self.amount,)
        self.__balance = (self.__balance,)

        return f"거래 타입 : {self.transaction_type}\n거래 금액 : {self.amount}\n거래 후 잔고 : {self.__balance}"
    
    
a = Transaction("입금", 1000, 500)

print(a.__str__())
print(a.to_tuple())
