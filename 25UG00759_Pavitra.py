exp = input("Enter infix expression: ")

# Step 1: Reverse expression
exp = exp[::-1]

# Swap brackets
exp = exp.replace("(", "#")
exp = exp.replace(")", "(")
exp = exp.replace("#", ")")

stack = []
postfix = ""

# Step 2: Convert to postfix
for ch in exp:

    if ch.isalnum():
        postfix += ch

    elif ch == "(":
        stack.append(ch)

    elif ch == ")":
        while stack and stack[-1] != "(":
            postfix += stack.pop()
        stack.pop()

    else:
        while stack and stack[-1] != "(":
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

# Step 3: Reverse postfix
prefix = postfix[::-1]

print("Prefix:", prefix)