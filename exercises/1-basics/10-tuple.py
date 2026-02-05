# ============================================
# 튜플(Tuple)이란?
# 여러 값을 묶어 저장하는 자료형 (리스트와 유사하지만 수정 불가능)
# 고정형 데이터, 좌표 등에 사용
# ============================================

# 리스트: 대괄호 [] 사용, 수정 가능 (mutable)
my_list = [1, 2, 3]
my_list[0] = 10  # 수정 가능
print(my_list)  # [10, 2, 3]

# 튜플: 소괄호 () 사용, 수정 불가능 (immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ 에러! 튜플은 수정 불가능
print(my_tuple)  # (1, 2, 3)

# 튜플 생성 방법
tuple1 = (1, 2, 3)           # 소괄호 사용
tuple2 = 1, 2, 3             # 소괄호 생략 가능
tuple3 = tuple([1, 2, 3])    # 리스트를 튜플로 변환

print(tuple1)  # (1, 2, 3)
print(tuple2)  # (1, 2, 3)
print(tuple3)  # (1, 2, 3)

# 튜플의 특징
# 1. 수정 불가능 (immutable)
# 2. 순서가 있음 (인덱스로 접근 가능)
# 3. 중복 허용

###### 심화 ######
# 튜플 접근
coordinates = (10, 20)
x = coordinates[0]  # 10
y = coordinates[1]  # 20
print(f"x: {x}, y: {y}")

# enumerate()가 반환하는 것도 튜플!
fruits = ["apple", "banana", "orange"]
for item in enumerate(fruits):
    print(item)  # (0, 'apple'), (1, 'banana'), (2, 'orange')
    print(type(item))  # <class 'tuple'>

# 언패킹(unpacking): 튜플을 여러 변수로 분해
point = (5, 10)
x, y = point  # 튜플을 x, y로 분해
print(f"x: {x}, y: {y}")  # x: 5, y: 10

# enumerate()도 튜플을 반환하므로 언패킹 가능
for idx, fruit in enumerate(fruits):  # (idx, fruit) = (0, 'apple')
    print(f"{idx}: {fruit}")