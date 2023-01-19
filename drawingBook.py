# https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem


def pageCount(n, p):
    end = n + 1 if n % 2 == 0 else n
    from_the_beginning = p
    from_the_end = end - p

    minimum_pages = min(from_the_beginning, from_the_end)

    return minimum_pages // 2


print(pageCount(6, 2))  # 1
print(pageCount(5, 3))  # 1
print(pageCount(5, 4))  # 0
print(pageCount(15, 10))  # 2
