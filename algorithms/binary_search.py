def binary_search(arr, val, low, high):
  if low > high:
    return False #해당 배열에 타겟 숫자 미존재

  mid = (low+high)//2 #탐색 기반이 되는 위치

  if arr[mid] > val:
    return binary_search(arr, val, low, mid -1) #수가 중앙 값보다 작을 때
  elif arr[mid] < val:
    return binary_search(arr, val, mid + 1, high) #수가 중앙 값보다 높을 때
  else:
    return True #수가 정중앙에 위치

print(binary_search([1,3,5,6,10], 6, 1, 10))