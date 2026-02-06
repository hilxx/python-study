# ============================================
# 함수 (Function)
# ============================================
# 함수는 특정 작업을 수행하는 코드 블록을 재사용 가능하게 만듭니다
# def 키워드로 함수를 정의합니다

# 1. 기본 함수 (매개변수 없음)
def say_hello():
    print("Hello!")

say_hello()  # Hello!

# 2. 매개변수가 있는 함수
def greet(name):
    print(f"Hello, {name}!")

greet("Jenny")  # Hello, Jenny!
greet("Tom")    # Hello, Tom!

# 3. 반환값(return)이 있는 함수
def add(a, b):
    return a + b  # return으로 값을 반환

result = add(3, 5)
print(result)  # 8

# 4. 여러 매개변수
def multiply(x, y, z):
    return x * y * z

result = multiply(2, 3, 4)
print(result)  # 24

# 5. 기본값(기본 인자)이 있는 함수
def greet_with_title(name, title="님"):
    print(f"안녕하세요, {name}{title}!")

greet_with_title("은정")           # 안녕하세요, 은정님!
greet_with_title("은정", "씨")     # 안녕하세요, 은정씨!

# 6. 여러 값을 반환하는 함수 (튜플로 반환)
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result  # 튜플로 반환

result1, result2 = calculate(10, 3)
print(f"합: {result1}, 차: {result2}")  # 합: 13, 차: 7

# 7. 함수의 장점
# - 코드 재사용: 같은 코드를 여러 번 쓰지 않아도 됨
# - 가독성: 코드가 더 읽기 쉬워짐
# - 유지보수: 한 곳만 수정하면 모든 곳에 적용됨

# 예: 점수 등급 계산 함수
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(get_grade(95))  # A
print(get_grade(85))  # B
print(get_grade(65))  # F

# 8. 함수 안에서 함수 호출 가능
def square(x):
    return x * x

def add_squares(a, b):
    return square(a) + square(b)

result = add_squares(3, 4)
print(result)  # 9 + 16 = 25