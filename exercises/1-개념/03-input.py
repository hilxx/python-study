age = 20
name = "Jenny"
height = 180

print(age)
print(name)
print(height)

print(type(age)) #<class 'int'>
print(type(name)) #<class 'str'>
print(type(height)) #<class 'int'>

name = input("What is your name? ")
print("Hello, ", name)

# input은 항상 문자열이다. (str)
# input은 사용자가 입력한 값을 출력한다.

# 숫자로 쓰려면 변환해야한다.
age = int(input("How old are you?")) # int()는 문자열을 숫자로 변환해주는 함수 > 문자열을 쓰면 value error가 발생함
print("You are ", age, "years old")

# 아.. 사용자가 아무것도 입력 안하고 enter치면 빈 문자열이 값에 전달되는구나😮
# 터미널에서 상호작용이 되어서 신기하군

# 그러면 최상단에 name = "Jenny" 이렇게 썼다가 아래에 name을 재정의하면서 값이 바뀌는거구나
# 사용자가 입력한 문자열이 name에 새로 들어가고, 이전에 있던 "Jenny"는 더 이상 사용되지 않습니다.
# 즉, 같은 변수 이름에 다른 값을 다시 넣으면, 항상 "마지막에 넣은 값"이 유효한 값이 됩니다.