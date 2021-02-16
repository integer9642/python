scores = [85, 92, 88, 71]
print(scores)
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[-1]) #역색인

print(len(scores)) #list의 길이

scores.append(90) #리스트 제일 마지막 색인에 추가
print(scores)

scores.remove(88) #리스트 삭제 scores[3]에 있던 값 71이 scores[2]로 이동
print(scores)

print(scores[2]) 

scores.insert(2, 77) #2번째 색인에 77 삽입
print(scores)

scores.pop(2) #2번째 색인 삭제
print(scores)

scores.sort() #오름차순 정렬
print(scores)

scores.sort(reverse=True) #역순 True 시작은 대문자
print(scores)

scores.clear() #모든 색인 삭제
print(scores)
