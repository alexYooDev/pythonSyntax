#순열(Permutation) : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열 
#eg = {'A','B','C'} -> 'ABC','ACB','BAC', 'CAB', 'CBA'
# nPr = n*(n-1)*(n-2)*....(n-r+1)

from itertools import combinations, permutations, product, combinations_with_replacement

data = ['A', 'B', 'C']
result = list(permutations(data,3))
print(f'모든 순열{result}')

#중복 순열 -> 2개를 뽑는 모든 순열
result1 = list(product(data, repeat=2))
print(f'중복된 2개 고르기{result1}')

# 조합(Combination) : 서로 다른 n개에서 순서와 상관없이 서로 다른 r개 선택
#eg = {'A','B','C'} -> 'AB' 'AC' 'AB'
# nCr = (n*((n-1*n-2*...*(n-r+1)))/r! 
result2 = list(combinations(data,2))
print(f'모든 2개 조합{result2}')

#중복조합
result3 = list(combinations_with_replacement(data,2))
print(f'중복된 2개 뽑는 모든 조합{result3}')