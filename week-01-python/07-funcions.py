# 함수 funtions 간략하고 보기쉽게 짜는 기법, 여러개를 수정해야할때 중복을 단순하게 바꿔준다
# 입력값 parameters, 반환값 return


def hello_friends(name):
    print("hello, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"


# print("hi, {}".format(name1))
# print("hi, {}".format(name2))
# print("hi, {}".format(name3))
# print("hi, {}".format(name4))
# print("hi, {}".format(name5))
# print("hi, {}".format(name6))
# print("hi, {}".format(name7))
# print("hi, {}".format(name8))


hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)


# 1)입력값 o  반환값 o #반환값이 있다는건 return이 있다는거 ,반환값이 있다는건 변수를 다룰수 있다
def sum(a, b):
    return a + b
# 2)입력값 o 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))
#3)입력값 x 반환값 o
def return_1():
    return 1

num_1 = return_1()
print(num_1)


#4) 입력값 x 반환값 x
def hello_world():
    print("hello world")
