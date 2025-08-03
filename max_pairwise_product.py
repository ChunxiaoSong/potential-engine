def max_pairwise_product(A):
    n = len(A)
    index=0
    for i in range (1,n):
        if A[i]>A[index]:
            index=i
    A[index], A[n-1] = A[n-1],A[index]
    index =0
    for i in range(1, n-1):
        if A[i]>A[index]:
            index=i
    A[index], A[n - 2] = A[n - 2], A[index]
    return A[n-2]*A[n-1]


if __name__ == '__main__':
    _ = int(input())
    A = list(map(int, input().split()))
    print(max_pairwise_product(A))
