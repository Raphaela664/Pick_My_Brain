def solution(A, K):
    if not A:
        return A

    K = K % len(A)
    print(K)
    return A[K:] + A[:K]

solution([1, 2, 3, 4], 5)


def fast_solution(n):
    result = n * (n + 1) // 2 #sum of n elements
    result1= (n+1) * (n+2)//2 # sum of n+1 elements
    return result

print(fast_solution(7))