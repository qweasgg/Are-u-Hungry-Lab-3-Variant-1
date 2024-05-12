# Are u Hungry - lab 3 - variant 1

Our group's variant is "Mathematical expression by expression tree." In this
experiment, we are required to build an interpreter that utilizes expression
trees to compute the input result of an expression.Simultaneously, implement
the visualization of the data flow graph.

## Project structure

- `expression_tree.py` -- implementation of `ExpresssionTree` class and `MathInterpreter` class
   Stateless.
- `expression_tree_test.py` -- unit and PBT tests for `MathInterpreter`.

## Features

- PBT: `test_interpreter`

## Contribution

- Yang Ao (1031901332@qq.com) -- Source code.
- Ying Yi (1812742922@qq.com) -- PBT test.

## Changelog

- 05.05.2024 - 0
  Initial

## Design notes

- Design Input Language:
  The input language should be a string representing a mathematical expression,
  for example, the input string could be like "a + 2 - sin(-0.3)*(b - c)".
- Design Type:
  Design an appropriate data structure to represent an expression tree, where each internal
  node represents an operator and each leaf node represents an operand.
- Implement Interpreter Functionality:
  1. Parse the input string into an expression tree.
  2. Calculate the value of the expression based on the expression tree.
  3. Support user-defined functions.
  4. Handle runtime errors and provide detailed error messages.
- Write test cases, including simple expressions, complex expressions, and edge cases.
