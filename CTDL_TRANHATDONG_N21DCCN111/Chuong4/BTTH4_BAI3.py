def GiaTri(bt):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def applyOp(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
    tokens = []
    i = 0
    while i < len(bt):
        if bt[i] == ' ':
            i += 1
            continue
        if bt[i] in "0123456789":
            j = i
            while j < len(bt) and bt[j] in "0123456789":
                j += 1
            tokens.append(int(bt[i:j]))
            i = j
        else:
            tokens.append(bt[i])
            i += 1
    values = []
    ops = []
    for token in tokens:
        if isinstance(token, int):
            values.append(token)
        else:
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(token)):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))
            ops.append(token)

    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(applyOp(val1, val2, op))

    return values[-1]
bt = "10 + 2 * 6"
print(f"Giá trị của biểu thức '{bt}' là: {GiaTri(bt)}")
