def merge_sort_string(s):
    if len(s) <= 1:
        return s

    # Divide the string into two halves
    mid = len(s) // 2
    left_half = s[:mid]
    right_half = s[mid:]

    # Recursively sort each half
    left_half = merge_sort_string(left_half)
    right_half = merge_sort_string(right_half)

    # Merge the sorted halves
    return merge_string(left_half, right_half)

def merge_string(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare characters from both strings and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining characters from left and right strings
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return ''.join(merged)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    first_sorted = merge_sort_string(first_string.lower())
    second_sorted = merge_sort_string(second_string.lower())

    if first_string == "" or second_string == "":
        return (first_sorted, second_sorted, False)

    if first_sorted == second_sorted:
        return (first_sorted, second_sorted, True)

    return (first_sorted, second_sorted, False)
