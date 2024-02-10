def solution(A):
    # Calculate the total sum of all elements in the array
    total_sum = sum(A)

    # Initialize the minimal difference to a large value
    min_difference = float('inf')

    # Initialize the left sum to 0
    left_sum = 0

    # Iterate through the array
    for num in A[:-1]:
        # Update the left sum
        left_sum += num

        # Calculate the right sum
        right_sum = total_sum - left_sum

        # Calculate the absolute difference
        difference = abs(left_sum - right_sum)

        # Update the minimal difference if necessary
        min_difference = min(min_difference, difference)

    return min_difference


# Example usage:
A = [3, 1, 2, 4, 3]
print(solution(A))  # Output: 1
