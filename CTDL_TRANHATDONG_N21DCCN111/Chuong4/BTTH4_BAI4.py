def HauTo(bt):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return -1

    def isOperand(c):
        return c.isdigit()
    tokens = []
    i = 0
    while i < len(bt):
        if bt[i] == ' ':
            i += 1
            continue
        if isOperand(bt[i]):
            j = i
            while j < len(bt) and isOperand(bt[j]):
                j += 1
            tokens.append(bt[i:j])
            i = j
        else:
            tokens.append(bt[i])
            i += 1

    ops = []
    postfix = []
    for token in tokens:
        if isOperand(token):
            postfix.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                postfix.append(ops.pop())
            ops.pop()
        else:
            while ops and precedence(ops[-1]) >= precedence(token):
                postfix.append(ops.pop())
            ops.append(token)

    while ops:
        postfix.append(ops.pop())

    return ' '.join(postfix)

bt = "2 + 3 * 5"
print(f"Biểu thức hậu tố của '{bt}' là: {HauTo(bt)}")
