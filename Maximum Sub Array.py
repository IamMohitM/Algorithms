def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float("-inf")
    right_sum = float("-inf")
    max_left = float("inf")
    max_right = float("inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for j in range(mid + 1, high + 1, 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(A, low, high):
    if low == high:
        print(low,high,A[low])
        return low, high, A[low]
    else:
        mid = (low + high) // 2

        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        print("c ", cross_low,cross_high,cross_sum)

    if left_sum >= right_sum and left_sum >= cross_sum:

        print("Left ", left_low, left_high, left_sum)
        return left_low, left_high, left_sum
    elif right_sum > left_sum and right_sum >= cross_sum:
        print("Right ",right_low, right_high, right_sum)
        return right_low, right_high, right_sum
    else:
        print("Cross ",cross_low, cross_high, cross_sum)
        return cross_low, cross_high, cross_sum


a = [ -3, -16, -23, 18, 20, -7, 12, -5]
print(find_max_subarray(a, 0, len(a) - 1))
