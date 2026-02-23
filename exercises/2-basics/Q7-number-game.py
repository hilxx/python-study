# 문제7 : 숫자 맞추기 게임
## 숫자 맞추기 게임을 작성하시오.

my_number = 3734

input_number = int(input("숫자를 입력하세요: "))

if input_number > my_number:
  print("너무 큽니다")
elif input_number < my_number:
  print("너무 작습니다")
else:
  print("정답입니다")

#########
# 정답 입력할 때까지 반복하기 (while 문 사용)
while True:
  try:
    input_number = int(input("숫자를 입력하세요: "))
    if input_number > my_number:
      print("너무 큽니다")
    elif input_number < my_number:
      print("너무 작습니다")
    else:
      print("정답입니다")
      break
  except ValueError:
    print("숫자를 입력해주세요")