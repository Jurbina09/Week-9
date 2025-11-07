"""
 Instructions: Write a function (use template below to get started)
 that takes a list of integers and returns a list of only the positive
 even numbers, doubled. Add at least one error-handling condition

For submission, commit and push the edited file to Github

"""

# Start the function (start of template)
def getDoublePositiveEvens(numbersList): 
    result = []
    # Go through each number in a list
    for num in numbersList:
        # Error handling: make sure each element is an integer
        if not isinstance(num, int):
            continue  # skip non-integer values

        # Check if the number is positive and even
        if num > 0 and num % 2 == 0:
            # Double the number and add it to the final list
            result.append(num * 2)

    return result


myNumbers = [1, 2, "hello", -4, 6, None, 8]
result = getDoublePositiveEvens(myNumbers)
print(result); # Output: [4, 12, 16]
