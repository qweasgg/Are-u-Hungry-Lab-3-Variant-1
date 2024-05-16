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

- PBT: `test_interpreter`

## Contribution

- Yang Ao (1031901332@qq.com) -- Source code.
- Ying Yi (1812742922@qq.com) -- PBT test.

## Changelog

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
