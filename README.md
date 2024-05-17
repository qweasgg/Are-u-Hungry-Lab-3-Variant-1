# Are u Hungry - lab 3 - variant 1

Our group's variant is "Mathematical expression by expression tree." In this
experiment, we are required to build an interpreter that utilizes expression
trees to compute the input result of an expression.Simultaneously, implement
the visualization of the data flow graph.

## Project structure

- `expression_tree.py` -- implementation of `ExpresssionTree` class
   and `MathInterpreter` class.
- `expression_tree_test.py` -- unit and PBT tests for `MathInterpreter`.

## Features

- Test: `test_evaluate` test the basic function of interpreter
  Test: `test_validate_input` test if the input data is invalid
  Func: `validate_input` used to validate input
  Func: `build_expression_tree`used to buld tree
  Func: `infix_to_postfix`used to create postfix for expression
  Func: `evaluate` used to calculate result
  Func: `visualize_tree` used to visualize the expression tree
  Func: `prase_expression` used to run the whole process

## Contribution

- Yang Ao (1031901332@qq.com) -- Source code.
- Ying Yi (1812742922@qq.com) -- PBT test.

## Changelog

- 17.05.2024 - 3
  Implementing input validate.
  Add some exception process.
  Implement test.
  Update README.

- 16.05.2024 - 2
  Implementing visualization.
  Implementing Python logging.

- 13.05.2024 - 1
  Implementing basic functionalities to build expression trees
  and evaluate expression results.
  Implementing functionalities to support user-defined functions.

- 05.05.2024 - 0
  Initial

## Design notes

- Design Input Language:
  The input language should be a string representing a mathematical expression,
  for example, the input string could be like "a + 2 - sin(-0.3)*(b - c)".
- Design Type:
  Design an appropriate data structure to represent an expression tree, where
  each internal node represents an operator and each leaf node
  represents an operand.
- Implement Interpreter Functionality:
    Parse the input string into an expression tree.
    Calculate the value of the expression based on the expression tree.
    Support user-defined functions.
    Handle runtime errors and provide detailed error messages.
- Write test cases, including simple expressions, complex expressions, and edge cases.
