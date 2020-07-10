def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashpos = {}
    hashneg = {}
    for item in a:
        if item > 0:
            hashpos[item] = item
        elif item < 0:
            hashneg[-item] = item
    # print(hashpos)
    # print(hashneg)


    result = []
    for item in hashpos:
        if item in hashneg:
            result.append(item)

    print("Result", result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
