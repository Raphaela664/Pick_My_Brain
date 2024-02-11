def solution(A):
    # Implement your solution here
    i=1
    if len(A) != len(set(A)):
        return 0
    arr_sorted=sorted(A)
    for j in arr_sorted:
        if j!=i :
            return 0
        i+=1
    return 1

print(solution([4, 1, 3, 2]))
