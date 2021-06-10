#다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

a = dict()
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
a[[1]] = 'python' #Error list elements can be varied: not suitable for key's atomicity
print(a)
a[250] = 'python'
print(a)

answer = "Error list elements can be varied: not suitable for key's atomicity"
print(answer)