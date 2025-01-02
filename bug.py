def function_with_uncommon_error(x):
    if x == 0:
        return 0  # This is correct
    elif x > 0:
        return 1 / x
    else:
        return 1 / x  # Error prone: Division by zero if x is a negative integer

# Example usage demonstrating the problem:
result = function_with_uncommon_error(-1)
print(result)  # This will cause a ZeroDivisionError

# Another scenario for the error:
# Suppose x was intended to be the absolute value. 
# Then, the below would be the correct logic.

# def function_with_uncommon_error(x):
#     if x == 0:
#         return 0 
#     elif x > 0:
#         return 1 / x
#     else:
#         return 1 / abs(x) # Correct logic

# result = function_with_uncommon_error(-1) 
# print(result)  #Output 1.0