#sum() -> add every elements in a list or a tuple

result = sum([1,2,3,4,5])
print(result)

# min(), max() -> gives min or max value in a number set

min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(f'minimun is {min_result}, and maximum is {max_result}')

# sorted() -> returns the sorted version of a list
result = sorted([9,1,8,5,4])  
# ascending sort
reverse_result = sorted([9,1,8,5,4], reverse=True)
# descending sort
print(f'asc={result}, dsc={reverse_result}')

#sorted() with key
arr = [('alex', 27),('kim', 28),('john', 49)]
result = sorted(arr, key=lambda x: x[1], reverse=True) # x equvalents to each element in the list
print(result)

# eval() -> returns the result of certain expression
result = eval("(3+5)*7")
print(result)

