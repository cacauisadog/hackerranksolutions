def icecreamParlor(m, arr):
    answer = []
    values_map = {k: i for i, k in enumerate(arr)}

    for i, element in enumerate(arr):
        compliment = m - element
        if compliment in values_map and values_map[compliment] != i:
            # the exercise demands 1-based indexing for some reason
            answer.append(i + 1)
            answer.append(values_map[compliment] + 1)
            break

    return answer
