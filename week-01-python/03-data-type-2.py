#목록 list.tuple
#사전 dictionary
#집합 set

#list[]
print("list")
print([1, 2, 3])
print(type([1,2,3]))

list_a = [1, 2, 3]
print(list_a[1])#INDEX는 0부터 시작이라 2가나옴
print(list_a[0:1])#리스트의 0부1까지 슬라이스 한다는 의미 마지막은 표시가 안됨

list_a.append(4)#추가
print(list_a)


list_a.remove(2)#2지우기
print(list_a)

list_a.clear()#모두지우기
print(list_a)


print("----------------")



#tuple(1,)
print("tuple")
print((1, 2, 3))
print(type([1,2,3]))

#list는 수정가능 tuple 변경불가

print("----------------")


#dict (map) {}
#key & value
dict_a = {
"apple" : "a type of fruits" , "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])

dict_a["pen"] = "something to write"
print(dict_a)
#edit value

print("-------------------")

#set set ([]) - 집합
set_a = set([1, 2, 3])#3을 여러개 넣어도 표시는 숫자 3하나만 출력  중복이 자동으로 제거
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

#리스트는 여러개 목록 나열 #집합은 중복이 불가능

print(set_a & set_a)#교집합
print(set_a | set_a)#합집합
print(set_a - set_a)#차집합
