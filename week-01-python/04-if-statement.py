#참과 거짓 boolean
#if
# true, false
# and, or, not


# 0은 거짓 1은 참


a = True
b = False

# A가 참이거나 혹은 B가 참이라면 (A나B중에 참)
print(a and b)# Flase
# A가 참이고, 혹은 B가 참이라면 (A와B 둘다참)
print(a or b)# True

print("--------------")


a = True
a == True

print(a ==True)
print(a is True)


print("------------------")


d = 7
if d >10:
    print ("변수는 10보다 큽니다")
elif d > 5 and d <= 10: #조건이 중첩된다면 
    print("변수는 10보다 작거나 같고 5보다는 큽니다")
else:#아니라면
    print("변수는 5보다 작거나 같습니다.")
