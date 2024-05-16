import re
import math
import logging
import matplotlib.pyplot as plt
import networkx as nx

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parameters = []


class ExpressionTreeInterpreter:
    def __init__(self, user_functions=None):
        self.operators1 = {  # Operator with one parameter
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x))
        }
        self.operators2 = {  # Operator with two parameters
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y,
        }
        self.user_functions = user_functions or {}

    def build_expression_tree(self, expression):
        # Convert to postfix expression
        postfix_expression = self.infix_to_postfix(expression)
        logger.debug(f"Postfix expression: {postfix_expression}")
        # Build expression tree
        stack = []
        for token in postfix_expression:
            if token not in self.operators1 and\
               token not in self.user_functions\
               and token not in self.operators2:
                # number or valuable
                stack.append(TreeNode(token))
                logger.debug(f"Created leaf node with value: {token}")
            else:
                # operator
                if token in self.operators1:  # operator with one parameter
                    node = TreeNode(token)
                    node.left = stack.pop()
                    logger.debug(f"Created node for operator '{token}'\
                                with left child {node.left.value}")
                elif token in self.user_functions:
                    # user function with muitiply parameters
                    node = TreeNode(token)
                    for _ in \
                            range(
                            len(
                            self.user_functions[token].__code__.co_varnames)):
                        arg_node = stack.pop()
                        node.parameters.append(arg_node)
                        logger.debug(f"Created node for user\
                                    function '{token}'\
                                    with parameters\
                                {[param.value for param in node.parameters]}")
                else:  # operator with two parameters
                    node = TreeNode(token)
                    node.right = stack.pop()
                    if not stack:
                        stack.append(TreeNode(str(0)))
                    node.left = stack.pop()
                    logger.debug(f"Created node for operator '{token}'\
                                with children {node.left.value}\
                                and {node.right.value}")
                stack.append(node)
        return stack[0]

    def infix_to_postfix(self, expression):
        # Levels of precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, 'sin': 4}
        for func in self.user_functions:
            precedence[func] = 4
        output = []
        stack = []
        tokens = re.findall(r'[a-zA-Z]+|\d+|\-|[-+*/^()]|sin|cos|tan',
                            expression)
        for i, token in enumerate(tokens):
            if token.isalpha() and token not in self.operators1\
               and token not in self.user_functions\
               and token not in self.operators2:
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
        try:
            if expression_tree:
                if expression_tree.value in self.operators1\
                   or expression_tree.value in self.operators2:
                    if expression_tree.right is not None:
                        left_val = self.evaluate(expression_tree.left,
                                                 variable_values)
                        right_val = self.evaluate(expression_tree.right,
                                                  variable_values)
                        func = self.operators2[expression_tree.value]
                        result = func(left_val, right_val)
                        logger.debug(f"Evaluating function\
                                    {expression_tree.value} with args\
                                    {left_val, right_val} = {result}")
                        return result
                    else:
                        left_val = self.evaluate(expression_tree.left,
                                                 variable_values)
                        func = self.operators1[expression_tree.value]
                        result = func(left_val)
                        logger.debug(f"Evaluating function\
                                     {expression_tree.value} with args\
                                     {left_val, right_val} = {result}")
                        return result
                elif expression_tree.value.isdigit() or\
                    (expression_tree.value[0] == '-' and
                     expression_tree.value[1:].isdigit()):
                    return float(expression_tree.value)
                elif (expression_tree.value.isalpha() and
                      expression_tree.value not in self.user_functions):
                    return variable_values.get(expression_tree.value, 0)
                else:
                    args = []
                    func = self.user_functions[expression_tree.value]
                    for token in expression_tree.parameters:
                        if token.value.isdigit():
                            args.append(float(token.value))
                        elif token.value.isalpha():
                            args.append(float(
                                        variable_values.get(token.value, 0)))
                        else:
                            args.append(float(token.value))
                    args.reverse()
                    result = func(*args)
                    logger.debug(f"Evaluating function\
                                 {expression_tree.value} with args\
                                 {args} = {result}")
                    return result
            else:
                return None
        except ValueError as ve:
            logger.error(f"Data type error: {str(ve)}")
            raise RuntimeError(f"Data type error: {str(ve)}")
        except ZeroDivisionError:
            logger.error("Division by zero")
            raise RuntimeError("Division by zero")
        except Exception as e:
            logger.error(f"Error evaluating expression: {str(e)}")
            raise RuntimeError(f"Error evaluating expression: {str(e)}")

    def visualize_tree(self, tree):
        def add_edges(graph, node, parent=None):
            if node:
                node_id = id(node)
                graph.add_node(node_id, label=node.value)
                if parent:
                    graph.add_edge(parent, node_id)
                add_edges(graph, node.left, node_id)
                add_edges(graph, node.right, node_id)
                for param in node.parameters:
                    add_edges(graph, param, node_id)

        # Disable logging
        logging.disable(logging.CRITICAL)

        try:
            graph = nx.DiGraph()
            add_edges(graph, tree)

            pos = nx.spring_layout(graph)
            labels = {node: data['label'] for node,
                      data in graph.nodes(data=True)}
            plt.figure()
            nx.draw(graph, pos, labels=labels,
                    with_labels=True, node_size=1500,
                    node_color='skyblue', font_size=10,
                    font_weight='bold', arrows=True)
            plt.show()
        finally:
            # Re-enable logging
            logging.disable(logging.NOTSET)


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


# Test 4
user_functions = {'foo': lambda x, y, z: x / y + z}
expression = "a + 2 - foo(b, c, d)*(2 - 1)"
interpreter = ExpressionTreeInterpreter(user_functions)
tree = interpreter.build_expression_tree(expression)
variable_values = {'a': 1, 'b': 3, 'c': 2, 'd': 1}
result = interpreter.evaluate(tree, variable_values)
print("Expression Tree Built and Evaluated Successfully!")
print("Result:", result)
interpreter.visualize_tree(tree)
