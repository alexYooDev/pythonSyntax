#factorial function implemeted by iteration
def factorial_iterative(n):
  result = 1
  # multiplification from 1 to n
  for i in range(1, n+1):
    result *= i
  return result 

#factorial function implemeted by recursion
def factorial_recursive(n):
  # if n is smaller or equals to 1 : return 1
  if n <= 1:
    return 1
  # n! = n * (n-1)! 
  return n*factorial_recursive(n-1)

print(factorial_recursive(5))
