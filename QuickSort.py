def partition(A, p, r, count=0):
    count += len(A[p:r])
    pivot = A[p]
    i = p + 1
    for j in range(p + 1, r + 1):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    i -= 1
    A[p], A[i] = A[i], A[p]
    return A, i, count


def returnMedian(A, x, y, z):
    if (A[y] > A[x] > A[z]) or (A[y] < A[x] < A[z]):
        return x
    elif (A[x] > A[y] > A[z]) or (A[x] < A[y] < A[z]):
        return y
    else:
        return z


def quickSort(A, p, r, count=0, type='first'):
    if p < r:

        if type == 'last':
            A[p], A[r] = A[r], A[p]

        elif type == 'median':
            center_element = (p + r) // 2
            median_element = returnMedian(A=A, x=p, y=center_element, z=r)
            A[median_element], A[p] = A[p], A[median_element]

        A, i, count = partition(A, p, r, count)
        A, count = quickSort(A=A, p=p, r=i - 1, count=count, type=type)
        A, count = quickSort(A=A, p=i + 1, r=r, count=count, type=type)

    return A, count


if __name__ == "__main__":
    Array = [3, 8, 2, 5, 4, 9, 2, 1, 100, 0, -1]
    print(quickSort(Array, 0, len(Array)-1))
