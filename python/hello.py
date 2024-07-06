def odd_numbers(n: int):
    for i in range(n + 1):
        if i % 2 != 0:
            yield i

# 제너레이터 함수 사용 예시
odd_list = list(odd_numbers(16))

print(odd_list)
