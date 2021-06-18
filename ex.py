def solution(s):
    
    arr = list(s)
    print(arr.count("("))
    print(arr.count(")"))
  
    pair = arr.count("(") == arr.count(")")
    closed = arr[0] == "(" and arr[-1] == ")"
    if pair and closed:
        return True
    else: return False
    
solution("())(()")