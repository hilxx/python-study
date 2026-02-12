# ✔ if문은 반드시 들여쓰기(4칸)을 해야한다.
age = 20

age = int(input("당신의 나이는 무엇입니까?"))

if age > 18:
  print("성인입니다.")
else:
  print("미성년자입니다.")

######
score = 82

score = int(input("당신의 점수는 몇점입니까?"))

if score >= 90:
  print("A")
elif score >= 80:
  print("B")
else:
  print("C")


# bool
score = int(input("당신의 점수는 몇점입니까? "))
is_score = (score == 82)  # score가 82면 True, 아니면 False
print(is_score)