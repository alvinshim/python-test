# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print((f"hello, {name}"))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"

# print(f"hello, {name1}")
# print(f"hello, {name2}")
# print(f"hello, {name3}")
# print(f"hello, {name4}")

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)

# 일력값 o, 반환값 o
def sum(a, b):
    return a + b
# 일력값 o, 반환값 x
def hello_friends(name):
    print((f"hello, {name}"))
# 일력값 x, 반환값 o
def return_1():
    return 1
# 일력값 x, 반환값 x
def hello_world():
    print("hello world")


# return은 변수에 값을 담을 수 있게 한다
