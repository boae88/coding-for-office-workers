# exceptions

# ZeroDivisionError
# 1 / 0
def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

# 4 / 2 = 2
print(divide_by(4, 2))
print(divide_by(4, 0))



# 예외 만들기
# Exception
class EvenNumberDevisionError(Exception):
    pass

def divide_by_odd_number(first, second):#odd num 홀수
    if second % 2 == 0:
        raise EvenNumberDevisionError
    else:
        return first / second
