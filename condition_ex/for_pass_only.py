marks = [90, 24, 67, 60, 70] 

num = 0

for mark in marks:
  num += 1
  if mark >= 60:
    print("Congratulations! Student No.%d. You've passed the test" %num)
  else: continue

marks = [90, 25, 67, 45, 80]
for i in range(len(marks)):
    if marks[i] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (i+1))