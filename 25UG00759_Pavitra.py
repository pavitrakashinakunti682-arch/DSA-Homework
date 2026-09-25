def infix_to_prefix(expression):

    # Step 1
    rev = expression[::-1]
    rev = rev.replace('(', '#').replace(')', '(').replace('#', ')')
    print("Step 1:", rev)

    # Step 2
    stack = []
    postfix = ""

    for ch in rev:
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    print("Step 2:", postfix)

    # Step 3
    prefix = postfix[::-1]
    print("Step 3:", prefix)
    print("Final Prefix:", prefix)

    # Answer
    print("Answer:", eval(expression))


expression = input("Enter infix expression: ")

print("\nInfix:", expression)
infix_to_prefix(expression)