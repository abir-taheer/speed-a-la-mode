def mode(nums: list) -> list:
    """
    Return the most occurring item in a list
    :param nums: A numerical list
    :return: The item that appears the most in the list

    >>> list_mode([1, 2, 3, 1])
    [1]

    >>> list_mode([-1, -4, 9, 2, -4, 9, -4])
    [-4]

    >>> list_mode(["hello", 0, 2, 3, 2, "hello", "hello"])
    ['hello']
    """

    # Initialize two variables
    # Numbers will hold all unique items that appear in the provided list
    numbers = []

    # Frequency will store how many times each item at the same index of numbers appears in the provided list
    frequency = []

    modes = []

    # Check all items in the provided list
    for x in nums:

        # Check if it appears in numbers
        if x not in numbers:
            # If it does not appear in numbers, add it to numbers and to the frequency lists
            # They are both added at the same time and their indexes in each list will correspond to each other
            numbers.append(x)
            frequency.append(0)

        # Find the item in the numbers list and increment its counter at the same index of the frequency list
        frequency[numbers.index(x)] += 1

    # Return the item from the numbers list that has the same index as the index of the
    # highest number in the frequency list
    max_frequency = max(frequency)

    for x in range(len(frequency)):
        if frequency[x] == max_frequency:
            modes.append(numbers[x])
    return modes


name = "V1: Two Buckets"
