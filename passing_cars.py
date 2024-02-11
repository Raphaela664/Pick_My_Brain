def solution(A):
    # Implement your solution here
    big_count=0
    for i in range(len(A)-2):
        small_count=0
        if A[i] ==0:
            print(A[i])
            for j in range(i,len(A)):
                if A[j]==1:
                    print(A[j])
                    small_count+=1
            big_count+=small_count
    return big_count

print(solution([0, 1, 0, 1, 1]))

