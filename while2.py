has_owner = ''

while has_owner != '예' :

    my_money = int(input('자산을 입력하세요'))
    if my_money <= 0 :
        print('통행료를 지불할  없군요!')
        break
    
    is_space = input('우주정거장 인가요? (예/아니요)')

    if is_space == '예' :
        print('다시 처음으로 돌아갑니다.')
        continue

    has_owner = input('주인이 있나요? (예/아니요)')
    
    if has_owner == '예' :
        print('통행료를 지불하세요!')
    else :
        print('야호! 통과!!')
        print('주사위를 던져서 다시 실행!!')

print('프로그램을 종료합니다')
