#리스트 자르기

scores = [85, 71, 77, 90]
print(scores)

print(scores[1:3]) #1,3번째 행만 가져오기, 나머지값이 사라지는것은 아

print(scores)

sliced_scores = scores[1:3] #새로운 변수를 추가해서 값을 넣어주기

print(sliced_scores)

print(scores[2:4]) 
print(scores[2:]) #마지막 색인은 기입안해도 괜찮
print(scores[:2]) #첫번째도 ㄱㅊ
print(scores[:]) #처음 끝이 아닌 색인을 출

new_scores = scores #new_scores값이 변동이있으면 scores값에도 적용됨
new_scores.append(99)
print(new_scores)
print(scores)

new_scores = scores[:] #★중요★ new_scores값이 변동이있으면 scores값에 적용 안됨
new_scores.append(100)
print(new_scores)
print(scores)

very_new_scores = new_scores.copy() #copy()함수가 [:]와 같은 역할을 해줌
very_new_scores.append(0)
print(very_new_scores)
print(new_scores)
                    
