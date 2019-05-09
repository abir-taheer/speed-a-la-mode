def mode(L):
    # Make a bucket containing all of the numbers until the max
    frequencies = [0 for x in range(max(L) + 1)]

    # Make a variable to store the modes
    modes = []

    # Count how many times each number appears
    for x in L:
        frequencies[x] += 1

    # Record the max frequency in a variable
    m = max(frequencies)

    # Find all items that have the same frequency as max and add them to modes
    for x in range(len(frequencies)):
        if frequencies[x] == m:
            modes.append(x)

    return modes


name = "V2: Single Bucket Approach (Numbers only)"
