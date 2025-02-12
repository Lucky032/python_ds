arrs = [1, 1, 5, 5, 3, 3, 3, 3, 3]  # Changed 'arr' to 'arrs' to avoid variable conflict
result = 0
count = 0

for arr in arrs:  # Fixed syntax error: 'for arr in arrs[]' → 'for arr in arrs'
    if count == 0:
        result = arr  # Assign result when count is 0
    if arr == result:
        count = count + 1  # Increment count when arr matches result
    else:
        count = count - 1  # Decrement count when arr does not match result

print(result)
