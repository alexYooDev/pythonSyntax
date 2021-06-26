
import re

n = int(input())

temp = []
answer = []
cnt = 0

for i in range(n):
  temp.append(input())

for a in temp:
  answer.append(list(item[0] for item in re.findall(r"((.)\2*)", a)))

print(answer)


