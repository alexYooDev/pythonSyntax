def solver(in1, in2, in3):

  # minimum = 전달 받은 파라미터로 만든 리스트에서 최소값
  minimun = min([in1,in2,in3])
  check_list = []
  num = 0
  
  # check_list의 길이가 minimun 만큼 채워질 때까지
  while len(check_list) <= minimun:
    possible_range = [num//in1, num//in2, num//in3]
    feasibility = False
    for i in range(0, possible_range[0] + 1):
      for j in range(0, possible_range[1] + 1):
        for k in range(0, possible_range[2]+1):
          # 세 숫자롤 조합이 가능한 지 확인
          if in1 * i + in2 * j + in3 * k == num:
            # 가능하다면 checklist에 추가
            check_list.append(num)
            # 가능성을 True로 전환
            feasibility = True
            # 반복문 종료
            break
        else:
          continue
        break
      else:
        continue
      break
    # 조합할 수 없다면 False, check_list를 비운다
    if feasibility == False:
      check_list = []
    # num을 1씩 더함 
    num += 1
  #check_list의 첫 번째 수보다 1작은 수를 반환
  answer = check_list[0] - 1
  print(check_list)
  return answer

print(solver(7,11,17))