import itertools

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashsums = {}
    for index, w in enumerate(weights):
        hashsums[w] = index
    solution = []
    for index, w in enumerate(weights):
        if (limit - w) in hashsums:
            solution.append(index)
            solution.append(hashsums[limit-w])
            if len(solution) ==2:
                s = tuple(sorted(solution, reverse=True))
                return s           




    # for w in weights:
    #     print(w)

    # answer = []
    # combinations = itertools.combinations(weights, 2)
    # solution_weights = get_solution_weight(combinations)
    # print(solution_weights)
    # for i, w in enumerate(weights):
    #     if w == solution_weights[1]:
    #         answer.append(i)
    #     elif w == solution_weights[0]:
    #         answer.append(i)
    
    # if answer:
    #     print(answer)
    #     return answer
    # return None

# def get_combinations(i, r=2):
#     return itertools.combinations(i, 2)

# def get_solution_weight(combinations):
#     for c in combinations:
#         if c[0] + c[1] == limit:
#             return (c[1], c[0])


if __name__ == "__main__":
    weights = [4, 6, 10, 15, 16]
    length = len(weights)
    limit = 21
    solution = get_indices_of_item_weights(weights, length, limit)
    print(solution)

    # combinations = get_combinations(weights, 2)
    # for c in combinations:
    #     print(c)