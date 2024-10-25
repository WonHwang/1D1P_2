answer = -1
cnt = 0
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt, answer
    tmp = []
    i, j = p, q+1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            answer = tmp[t]
            return
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
merge_sort(A, 0, len(A)-1)
print(answer)