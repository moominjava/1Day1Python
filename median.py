# 리스트의 중강 값을 반환한다
# sort를 사용해서 리스트를 정렬한다
# 리스트가 홀수라면 중간 값을 반환한다
# 리스트가 짝수라면 중간 값 두 수의 평균을 구해 반환한다

def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return list[int(list_length / 2)]

median([1, 2, 3]) #2
median([1, 2, 3, 4]) #2.5