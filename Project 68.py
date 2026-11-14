#In this assignment, you will build a Python program that tracks array sums, checks left-right balance, finds an equilibrium point, grows a subarray window, and searches for a target sum. The activity helps you understand how arrays can be sliced, scanned, and checked using loops and conditions.
def track_sums(arr):
    total = sum(arr)
    running_sum = []
    current = 0
    for num in arr:
        current += num
        running_sum.append(current)
    return total, running_sum


def check_balance(arr, split_index):
    if split_index < 0 or split_index > len(arr):
        raise ValueError("Split index out of bounds.")
    
    left_part = arr[:split_index]
    right_part = arr[split_index:]
    
    left_sum = sum(left_part)
    right_sum = sum(right_part)
    
    is_balanced = (left_sum == right_sum)
    return is_balanced, left_sum, right_sum


def find_equilibrium_point(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i, num in enumerate(arr):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
        
    return -1


def growing_subarray_window(arr, target_sum):
    start = 0
    current_sum = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
            
        if current_sum == target_sum:
            return (start, end)
            
    return None


def search_target_sum(arr, target):
    subarrays = []
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == target:
                subarrays.append((i, j, arr[i:j+1]))
    return subarrays


if __name__ == "__main__":
    sample_array = [1, 3, 5, 2, 2]
    
    total, running = track_sums(sample_array)
    print(f"Array: {sample_array}")
    print(f"Total Sum: {total}")
    print(f"Running Sums: {running}\n")
    
    split = 3
    balanced, l_sum, r_sum = check_balance(sample_array, split)
    print(f"Split at index {split} -> Left sum: {l_sum}, Right sum: {r_sum}")
    print(f"Is balanced? {balanced}\n")
    
    eq_array = [1, 2, 3, 4, 3, 2, 1]
    eq_index = find_equilibrium_point(eq_array)
    print(f"Array: {eq_array}")
    print(f"Equilibrium Index: {eq_index}\n")
    
    window_array = [1, 2, 3, 7, 5]
    target = 12
    window_range = growing_subarray_window(window_array, target)
    print(f"Array: {window_array}, Target: {target}")
    print(f"Subarray indices found: {window_range}\n")
    
    search_array = [1, 2, 3, 4, 5]
    target_sum = 5
    matches = search_target_sum(search_array, target_sum)
    print(f"Array: {search_array}, Target: {target_sum}")
    print(f"Found matching subarrays: {matches}")