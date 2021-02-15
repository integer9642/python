has_owner = input('주인이 있나요? (예/아니요)')
 
if has_owner == '예' :
	print('통행료를 지불하세요!')
elif has_owner == '아니요' :
    print('야호! 통과!!')
else :
    print('잘못 입력했습니다')
