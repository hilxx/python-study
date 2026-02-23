# 문제4 : 1부터 10까지 출력
## 1부터 10까지 출력하는 프로그램을 작성하시오.

numbers = [10, 20, 30, 40, 50]

total = 0
for i in numbers:
  total += i # += 현재 변수(total) 값에 어떤 값(i)을 더해서 그 결과를 다시 그 변수(total)에 넣는다.

average = total / len(numbers)
print(f"평균: {average}")

