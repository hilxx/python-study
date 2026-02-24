# 문제8 : 세 수 중 가장 큰 수 구하기
## 사용자에게 정수 3개 입력받고 그 중 가장 큰 수 구하기.

num1 = int(input("첫 번째 정수를 입력해주세요: "))
num2 = int(input("두 번째 정수를 입력해주세요: "))
num3 = int(input("세 번째 정수를 입력해주세요: "))

if num1 > num2 and num1 > num3:
  print(f"가장 큰 수는 {num1}입니다.")
elif num2 > num1 and num2 > num3:
  print(f"가장 큰 수는 {num2}입니다.")
else:
  print(f"가장 큰 수는 {num3}입니다.")

# ============================================
# 참고: 다른 해결 방법들
# ============================================

# 방법 1: >= 사용 (같은 수일 때도 올바르게 동작)
# num1=5, num2=5, num3=3 인 경우 > 로 하면 else로 가서 num3가 나오는데,
# >= 를 쓰면 num1 >= num2 and num1 >= num3 가 True가 되어 num1 출력
if num1 >= num2 and num1 >= num3:
    print(f"[방법1] 가장 큰 수는 {num1}입니다.")
elif num2 >= num1 and num2 >= num3:
    print(f"[방법1] 가장 큰 수는 {num2}입니다.")
else:
    print(f"[방법1] 가장 큰 수는 {num3}입니다.")

# 방법 2: max() 내장 함수 사용 (가장 간결)
result = max(num1, num2, num3)
print(f"[방법2] 가장 큰 수는 {result}입니다.")