def solver(in1, in2, in3):
  minimun = min([in1,in2,in3])
  check_list = []
  num = 0
  while len(check_list) <= minimun:
    possible_range = [num//in1, num//in2, num//in3]
    feasibility = False
    for i in range(0, possible_range[0] + 1):
      for j in range(0, possible_range[1] + 1):
        for k in range(0, possible_range[2]+1):
          if in1 * i + in2 * j + in3 * k == num:
            check_list.append(num)
            feasibility = True
            break
        else:
          continue
        break
      else:
        continue
      break
    if feasibility == False:
      check_list = []
    num += 1
  answer = check_list[0] - 1
  return answer

print(solver(7,11,17))