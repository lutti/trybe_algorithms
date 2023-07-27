def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from both lists and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left and right lists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def check_correct_number_array(nums):
    if isinstance(nums, str):
        return False

    if not isinstance(nums, list):
        return False

    if not all(not isinstance(num, str) for num in nums):
        return False

    if not all(num >= 1 for num in nums):
        return False

    return True


def find_duplicate(nums):
    if check_correct_number_array(nums):
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                return sorted_nums[i]

    return False
