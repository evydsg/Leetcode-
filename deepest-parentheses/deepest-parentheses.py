def deepestParentheses(s: str):
    brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    maxDepth, depth = 0, 0
    result = 0
    start = 0

    for index, character in enumerate(s):
        if character in brackets.values():
            depth += 1
            stack.append(character)

            maxDepth = max(maxDepth, depth)
        
        elif character in brackets and len(stack) > 0 and stack[-1] == brackets[character]:
            stack.pop()
            depth -= 1
        
    stack = []
    depth = 0

    for index, character in enumerate(s):
        if character in brackets.values():
            depth += 1
            stack.append(character)

            if depth == maxDepth:
                start = index + 1
        
        elif character in brackets and len(stack) > 0 and stack[-1] == brackets[character]:
            stack.pop(0)

            if depth == maxDepth:
                result.append(s[start: index])
            depth -= 1
        
    return result
