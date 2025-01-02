def function_with_uncommon_error(x):
    if x == 0:
        return 0  # This is correct
    elif x > 0:
        return 1 / x
    else:
        return 1 / abs(x) # Correct logic: Handle negative input to avoid ZeroDivisionError

# Example usage demonstrating the fix
result = function_with_uncommon_error(-1)
print(result)  # Output: 1.0