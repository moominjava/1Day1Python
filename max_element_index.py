
# max(), arr.index()를 확용하여 가장큰 값의 리스트 인덱스 값을 얻을 수 있다
# 리스트의 가정큰 값은 :10  인덱스 값:4
def max_element_index(arr):  
  return arr.index(max(arr))


max_element_index([1, 5, 6, 9, 10, 3, 0])
