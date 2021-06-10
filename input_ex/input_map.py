# take the number of the students and then their test scores 
# make a list with their scores descending sorted

n = int(input())

scores = list(map(int, input().split()))
scores.sort(reverse=True)

print(scores)