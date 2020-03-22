import random


def mergeSort(A):
    length = len(A)
    if length <= 1:
        return A
    else:
        left = mergeSort(A[:length // 2])
        right = mergeSort(A[length // 2:])
        C = merge(left, right)
        return C


def merge(left, right):
    if left is None:
        return right
    elif right is None:
        return left
    len_left = len(left)
    len_right = len(right)
    i = 0
    j = 0
    mergeArray = []
    for k in range(len_left + len_right - 1):
        if left[i] < right[j]:
            mergeArray.append(left[i])
            if i + 1 < len_left:
                i += 1
            else:
                mergeArray.extend(right[j:])
                break
        else:
            mergeArray.append(right[j])
            if j + 1 < len_right:
                j += 1
            else:
                mergeArray.extend(left[i:])
                break
    return mergeArray


if __name__ == '__main__':
    A = [random.randint(0, 10000000) for i in range(100)]
    print('Done')
    print(mergeSort(A))
