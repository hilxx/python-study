# ============================================
# 오류 기본 대응 - try/except
# ============================================
# try-except는 에러가 발생할 수 있는 코드를 안전하게 처리하는 방법입니다

# 1. 기본 사용법
# try: 에러가 발생할 수 있는 코드
# except: 에러가 발생했을 때 실행할 코드

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Please enter a valid number")

# 동작 방식:
# - 사용자가 숫자를 입력하면 → 정상 실행
# - 사용자가 문자를 입력하면 → ValueError 발생 → except 블록 실행

# 2. 여러 에러 처리
try:
    num = int(input("Enter a number: "))
    result = 10 / num  # 0으로 나누면 ZeroDivisionError 발생
    print(f"10 / {num} = {result}")
except ValueError:
    print("숫자를 입력해주세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")

# 3. 모든 에러 처리 (권장하지 않음 - 구체적인 에러 처리 권장)
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:  # 모든 에러를 잡음
    print(f"에러 발생: {e}")

# 4. else: 에러가 발생하지 않았을 때 실행
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("숫자를 입력해주세요!")
else:
    print(f"입력한 숫자: {num}")  # 에러가 없을 때만 실행

# 5. finally: 에러 여부와 관계없이 항상 실행
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("숫자를 입력해주세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
finally:
    print("프로그램을 종료합니다.")  # 항상 실행됨

# 6. try-except 없이 에러가 발생하면?
# num = int(input("Enter a number: "))  # 숫자가 아니면 프로그램이 중단됨!

# 7. 실제 사용 예시
def get_age():
    while True:  # 올바른 입력을 받을 때까지 반복
        try:
            age = int(input("나이를 입력하세요: "))
            if age < 0 or age > 150:
                print("올바른 나이를 입력해주세요!")
                continue
            return age
        except ValueError:
            print("숫자를 입력해주세요!")

# age = get_age()
# print(f"당신의 나이는 {age}세입니다.")