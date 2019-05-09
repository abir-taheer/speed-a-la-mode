def mode(numbers):
    """Returns the modes of a list
    :param numbers: A list of numbers to find the mode from
    :return: A list containing all of the modes

    >>> mode([1,2,3,4,5,5])
    [5]

    >>> mode([1,6,1,7,1,2,3,2,5,2,6])
    [1, 2]

    >>> mode([])
    []
    """
    # Make a dictionary to store frequencies where key is the item and value is frequency
    frequencies = {}

    # Initialize a list to store the modes
    modes = []

    # Initialize the frequency list with all unique items
    for x in numbers:
        frequencies[x] = 0

    # Calculate the frequencies of all of the items in numbers
    for x in numbers:
        # Increment the frequency of that item in the frequencies dictionary
        frequencies[x] += 1

    # Initialize a variable to store the frequency of the item with the highest frequency
    max_frequency = 0

    # Loop through the list of all of the frequencies
    for num in frequencies:
        # Set a variable to the frequency of the current item because we reference it a lot
        frequency_of_num = frequencies[num]

        # If the frequency of the current item is greater than the previous max frequency
        if frequency_of_num > max_frequency:
            # Set this frequency to the new max frequency
            max_frequency = frequency_of_num

            # Remove all of the modes from the list
            modes = []

        # If this item has the same frequency as the max frequency, it is a mode
        # Add it to the list of modes
        if frequency_of_num == max_frequency:
            modes.append(num)

    # Return the list of modes
    return modes


name = "V3: Dictionary Approach"
