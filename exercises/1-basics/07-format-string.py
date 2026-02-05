# ============================================
# f-string (포맷 문자열)이란?
# ============================================
# 문자열 앞에 f를 붙이면 변수를 문자열 안에 직접 넣을 수 있습니다
name = "Jenny"
age = 20

# 방법 1: f-string (가장 권장!)
print(f"My name is {name} and I'm {age} years old")
# 출력: My name is Jenny and I'm 20 years old

# 방법 2: + 연산자 (불편함)
print("My name is " + name + " and I'm " + str(age) + " years old")

# 방법 3: format() 메서드 (구식)
print("My name is {} and I'm {} years old".format(name, age))

# f-string의 장점:
# - 읽기 쉬움
# - 변수 타입 자동 변환 (str() 불필요)
# - 중괄호 {} 안에 변수나 표현식 직접 사용 가능

# f-string에서 표현식 사용
x = 10
y = 20
print(f"{x} + {y} = {x + y}")  # 10 + 20 = 30