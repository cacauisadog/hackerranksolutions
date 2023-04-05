def isBalanced(s):
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    bracket_stack = []

    for b in s:
        if b in bracket_map:
            bracket_stack.append(b)

        else:
            if not bracket_stack:
                return "NO"

            last_bracket = bracket_stack.pop()
            if bracket_map[last_bracket] != b:
                return "NO"

    if bracket_stack:
        return "NO"

    return "YES"
