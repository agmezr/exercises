def regularBracketSequence2(sequence):

    stack = []
    for i in range(len(sequence)):
        if len(stack) > 0 and stack[len(stack) - 1] == '(' and sequence[i] == ')':
            stack.pop()
            continue
        if  len(stack) > 0 and stack[len(stack) - 1] == '[' and sequence[i] == ']' :
            stack.pop()
            continue
        stack.append(sequence[i])

    if len(stack) != 0:
        return False
    return True
