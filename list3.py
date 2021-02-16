#리스트 합치기
a=[1,2,3]
b=[4,5,6]

print(a)
print(b)
print(a+b)
c = a+b # a+b =c 하면 오류
print(c)

a.extend(b) #새로운 변수를 추가하지않고 a에 b를 합치는법
print(a)
