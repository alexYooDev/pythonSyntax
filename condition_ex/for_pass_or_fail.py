marks = [90, 24, 67, 60, 70]
stu_num = 0
for mark in marks:
  stu_num += 1
  if mark >= 60:
    print("student No.%d has passed the test" %stu_num)
  else: print("student No.%d failed the test" %stu_num)