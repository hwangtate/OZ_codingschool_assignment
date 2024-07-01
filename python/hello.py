price_inform = {
  "붕어빵 팥" : 2000,
  "붕어빵 슈크림" : 2500,
  "붕어빵 잡채" : 3000
}

count_inform = {
  "붕어빵 팥" : int(input("붕어빵 팥 : ")),
  "붕어빵 슈크림" : int(input("붕어빵 슈크림 : ")),
  "붕어빵 잡채" : int(input("붕어빵 잡채 : "))
}

total_pay = (count_inform["붕어빵 팥"] * price_inform["붕어빵 팥"]) + (count_inform["붕어빵 슈크림"] * price_inform["붕어빵 슈크림"]) + (count_inform["붕어빵 잡채"] * price_inform["붕어빵 잡채"])
""
print(f"지불해주세요. {total_pay}원을")
