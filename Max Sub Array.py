def find_max_crossing_subarray(array, low, mid, high):
    """Finds the maximum sub-array crossing the mid-point of an array"""
    left_sum = float("-inf")
    max_left = float("inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        # From mid goes left. Left sum is negative infinity and compares the sum to it. the sum is changed with each iteration
        # But the left_sum and max_left, which is the index the max subarray starts, are only changed when sum becomes greater than left_sum

        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float("-inf")
    max_right = float("inf")
    sum = 0
    for i in range(mid + 1, high + 1, 1):
        # Same as previous loop except moves from mid to high. max_right is where the max sub array ends
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(array, low, high):
    """Finds maximum sub array of an array. Uses Divide and conquer. Compares sum of sub-arrays from low to mid-point,\nmid point to high and the sub-arrays crossing the mid point."""
    if high == low:
        return low, high, array[low]
    else:
        # Dividing
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(array, low, mid)
        right_low, right_high, right_sum = find_max_subarray(array, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)

        # comparing and combining
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low, high, Max_sum = find_max_subarray(a, 0, len(a) - 1)
print(low + 1)  # Print lowest index of max sub-array
print(high + 1)  # Print highest index of max sub-array
print(Max_sum)  # Print sum of max sub-array
print(find_max_crossing_subarray.__doc__)
print(find_max_subarray.__doc__)
