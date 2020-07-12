# sorted()를 이용해서 리스트값을 정렬할 수 있다
# [:n]을 사용해서 n개의 값을 가져올 수 있다
# n개의 값을 가져오기 위해 슬라이싱을 사용한다

def min_n(lst, n=1):
  return sorted(lst, reverse=False)[:n]

min_n([1, 2, 3], 2) #1,2
min_n([1, 2, 3]) # 1