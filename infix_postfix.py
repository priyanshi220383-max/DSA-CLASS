# Function to return precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = []      # Stack to store operators
    result = ""     # Output postfix expression

    for char in expression:
        
        # If operand (letter/number), add to result
        if char.isalnum():
            result += char

        # If '(', push to stack
        elif char == '(':
            stack.append(char)

        # If ')', pop until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # Remove '('

        # If operator
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                result += stack.pop()
            stack.append(char)

    # Pop remaining operators
    while stack:
        result += stack.pop()

    return result


# Example usage
exp = "A+B*C"
print("Infix:", exp)

postfix = infix_to_postfix(exp)
print("Postfix:", postfix)