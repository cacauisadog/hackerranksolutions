# https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem
# Such a badly worded problem. It says "permutations", but what it really wants is simply for you reverse the arrays,
# not really check all the len factorial permutations.


def twoArrays(k, A, B):
    if _check_condition(k, A, B):
        return "YES"

    sorted_A = sorted(A)
    sorted_B = sorted(B)

    if _check_condition(k, sorted_A, sorted_B):
        return "YES"

    reversed_A = list(reversed(sorted_A))

    if _check_condition(k, reversed_A, sorted_B):
        return "YES"

    reversed_B = list(reversed(sorted_B))

    if _check_condition(k, sorted_A, reversed_B):
        return "YES"

    if _check_condition(k, reversed_A, reversed_B):
        return "YES"

    return "NO"


def _check_condition(k, A, B):
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return False
    return True


print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))
