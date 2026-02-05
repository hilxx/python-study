# 기본적인 for 문
for i in range(5):
    print(i) # 0부터 5개의 숫자 출력

for i in range(1, 6):
    print(i) # 1부터 6 전까지 (1, 2, 3, 4, 5) 출력

#range(5)        0부터 5 전까지 → 0, 1, 2, 3, 4
#range(1, 6)     1부터 6 전까지 → 1, 2, 3, 4, 5
#range(0, 5)     0부터 5 전까지 → 0, 1, 2, 3, 4
#range(2, 8)     2부터 8 전까지 → 2, 3, 4, 5, 6, 7

#range(0, 10, 2) 0부터 10 전까지, 2씩 증가 → 0, 2, 4, 6, 8
#range(1, 10, 3) 1부터 10 전까지, 3씩 증가 → 1, 4, 7

# 변수 이름은 자유롭게 변경 가능!
for a in range(3):
    print(a)

for num in range(3):
    print(num)

for index in range(3):
    print(index)
