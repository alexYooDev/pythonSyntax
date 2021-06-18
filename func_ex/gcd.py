def gcd(a,b):
  if a%b == 0:
    # a가 b의 배수가 되므로, 최소공약수는 b가 된다.
    return b
  else:
    # 나누어 떨어지지 않을 경우, b를 a를 b로 나눈 나머지와 다시 나눈다
    return gcd(b, a%b)

print(gcd(192,162))