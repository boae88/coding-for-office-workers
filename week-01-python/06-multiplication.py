#1) 사용자로부터 몇단을 출력할지 받을 것
#2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할것









dan = int(input("몇단을 출력하시겠습니까? "))#숫자로 입력해도 문자로 받는다
for num in range(1,10):# 마지막숫자는 제외됨
     print("{} * {}  ={}".format(dan, num, dan * num))#임의로빈공간 만들고 포맷으로 (스트링으로 만들어서 사용)
