def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)

def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right): 
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]: 
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1

def is_anagram(first_string, second_string):
    primeira_palavra = [*first_string.lower()]
    segunda_palavra = [*second_string.lower()]
    merge_sort(primeira_palavra)
    merge_sort(segunda_palavra)
    
    first_string = ''.join(primeira_palavra)
    second_string = ''.join(segunda_palavra)
    
    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)