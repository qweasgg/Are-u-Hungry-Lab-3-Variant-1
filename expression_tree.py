import re
import math


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parameters = []


class ExpressionTreeInterpreter:
    def __init__(self, user_functions=None):
        self.operators = {'+', '-', '*', '/', '^', 'sin'}
        self.user_functions = user_functions or {}

    def build_expression_tree(self, expression):
        # Convert to postfix expression
        postfix_expression = self.infix_to_postfix(expression)
        print(postfix_expression)
        # Build expression tree
        stack = []
        for token in postfix_expression:
            if token not in self.operators and \
               token not in self.user_functions:
                # number or valuable
                stack.append(TreeNode(token))
            else:
                # operator
                node = TreeNode(token)
                if token == 'sin':  # operator with only one parameter
                    node.left = stack.pop()
                elif token in self.user_functions:
                    # user function with muitiply parameters
                    node = TreeNode(self.user_functions[token])
                    for _ in \
                            range(
                            len(
                            self.user_functions[token].__code__.co_varnames)):
                        arg_node = stack.pop()
                        node.parameters.append(arg_node)
                else:  # operator with two parameters
                    node.right = stack.pop()
                    if not stack:
                        stack.append(TreeNode(str(0)))
                    node.left = stack.pop()
                stack.append(node)
        return stack[0]

    def infix_to_postfix(self, expression):
        # Levels of precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, 'sin': 4}
        for func in self.user_functions:
            precedence[func] = 4
        output = []
        stack = []
        tokens = re.findall(r'[a-zA-Z]+|\d+|\-|[-+*/^()]|sin', expression)
        for i, token in enumerate(tokens):
            if token.isalpha() and token not in self.operators\
               and token not in self.user_functions:
                # valuable
                output.append(token)
            elif token.isdigit():
                # number
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                # Determine whether '-' is a symbol or an operator
                if token == '-' and (i == 0 or tokens[i-1] in '([-+*/^'):
                    output.append('-' + tokens[i+1])
                    tokens.pop(i+1)
                    continue
                # Pop operators with greater precedence
                while (stack and
                       precedence.get(stack[-1], 0) >= precedence.get(token,
                                                                      0)):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def evaluate(self, expression_tree, variable_values):
        if expression_tree:
            if callable(expression_tree.value):
                args = []
                for token in expression_tree.parameters:
                    if token.value.isdigit():
                        args.append(float(token.value))
                    else:
                        args.append(float(variable_values.get(token.value, 0)))
                args.reverse()
                return expression_tree.value(*args)
            elif expression_tree.value.isdigit() or\
                (expression_tree.value[0] == '-' and
                 expression_tree.value[1:].isdigit()):
                return float(expression_tree.value)
            elif (expression_tree.value.isalpha() and
                  expression_tree.value != 'sin'):
                return variable_values.get(expression_tree.value, 0)
            elif expression_tree.value == 'sin':
                result = self.evaluate(expression_tree.left, variable_values)
                result_in_degrees = math.radians(result)
                sin_result = math.sin(result_in_degrees)
                return sin_result
            else:
                left_val = self.evaluate(expression_tree.left, variable_values)
                right_val = self.evaluate(expression_tree.right,
                                          variable_values)
                operator = expression_tree.value
                if operator == '+':
                    return left_val + right_val
                elif operator == '-':
                    return left_val - right_val
                elif operator == '*':
                    return left_val * right_val
                elif operator == '/':
                    return left_val / right_val
                elif operator == '^':
                    return left_val ** right_val

# # Test 1
# expression = "a + 2 - sin(-30)*(b - c)"
# interpreter = ExpressionTreeInterpreter()
# tree = interpreter.build_expression_tree(expression)
# variable_values = {'a': 1, 'b': 3, 'c': 2}
# result = interpreter.evaluate(tree, variable_values)
# print("Expression Tree Built and Evaluated Successfully!")
# print("Result:", result)

# # Test 2
# user_functions = {'foo': lambda x: x + 2}
# expression = "a + 2 - foo(-1)*(b - c)"
# interpreter = ExpressionTreeInterpreter(user_functions)
# tree = interpreter.build_expression_tree(expression)
# variable_values = {'a': 1, 'b': 3, 'c': 2}
# result = interpreter.evaluate(tree, variable_values)
# print("Expression Tree Built and Evaluated Successfully!")
# print("Result:", result)

# # Test 3
# user_functions = {'foo': lambda x, y: x ** y}
# expression = "a + 2 - foo(2, 3)*(b - c)"
# interpreter = ExpressionTreeInterpreter(user_functions)
# tree = interpreter.build_expression_tree(expression)
# variable_values = {'a': 1, 'b': 3, 'c': 2}
# result = interpreter.evaluate(tree, variable_values)
# print("Expression Tree Built and Evaluated Successfully!")
# print("Result:", result)

# # Test 4
# user_functions = {'foo': lambda x, y: x / y}
# expression = "a + 2 - foo(b, c)*(2 - 1)"
# interpreter = ExpressionTreeInterpreter(user_functions)
# tree = interpreter.build_expression_tree(expression)
# variable_values = {'a': 1, 'b': 3, 'c': 2}
# result = interpreter.evaluate(tree, variable_values)
# print("Expression Tree Built and Evaluated Successfully!")
# print("Result:", result)
