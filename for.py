for word in '재밌는 파이썬 프로그래밍' :
    print(word)
print('\n')

for n in range(10):
    print('파이썬을 배워봅시다!!')
print('\n')

for n in range(10) :
    print(n, '번 실행!!')
print('\n')

for n in range(1, 11 ) : #시작과 끝 범위 설정
    print(n, '번 실행!!')
print('\n')

for n in range(1, 11, 2) : #3번째 인수는 숫자가 증가되는 폭 설정
    print(n, '번 실행!!')
print('\n')

for n in range(1,11):
    if n%2 == 1 :
        continue
    print(n, '번 실행!!')
print('\n')

for n in range(1,11):
    if n%2 != 1 :
        continue
    print(n, '번 실행!!')
print('\n')
