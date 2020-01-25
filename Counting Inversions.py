def count_split(left_half, right_half, left_len, right_len):
    sorted_array = []
    count, i, j = [0] * 3
    for k in range(left_len + right_len - 1):
        if left_half[i] > right_half[j]:
            sorted_array.append(right_half[j])
            count += left_len - i
            j += 1
            if j >= right_len:
                sorted_array.extend(left_half[i:])
                break
        else:
            sorted_array.append(left_half[i])
            i += 1
            if i >= left_len:
                sorted_array.extend(right_half[j:])
                break
    return sorted_array, count


def count_inversions(A, length):
    if length == 1:
        return A, 0
    else:
        half_length = length // 2
        left_half = A[:half_length]
        right_half = A[half_length:]
        left_len = len(left_half)
        right_len = len(right_half)
        left_sorted, left_count = count_inversions(left_half, left_len)
        right_sorted, right_count = count_inversions(right_half, right_len)
        sorted_array, split_count = count_split(left_sorted, right_sorted,
                                                left_len, right_len)

        return sorted_array, left_count + right_count + split_count


if __name__ == "__main__":
    import random
    size = 100000
    A = [random.randint(1, 1000000000) for i in range(size)]
    A = [7, 6, 5, 4, 3, 2, 1]
    print(count_inversions(A, len(A)))
