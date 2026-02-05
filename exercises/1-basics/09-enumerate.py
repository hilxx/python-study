
# 인덱스와 값을 함께 사용할 때 - enumerate()
# enumerate()는 리스트를 순회할 때 인덱스와 값을 함께 가져오는 함수
# (인덱스, 값) 튜플을 반환합니다
fruits = ["apple", "banana", "orange"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")
# 출력:
# 0: apple
# 1: banana
# 2: orange

# enumerate() 없이 인덱스가 필요할 때 (비효율적)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# enumerate()의 두 번째 인자: start 파라미터로 시작 번호 지정
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}: {fruit}")
# 출력:
# 1: apple
# 2: banana
# 3: orange