import unittest
from hypothesis import given,  strategies

from expression_tree import ExpressionTreeInterpreter


class TestInterpreter(unittest.TestCase):

    def test_validate_input(self):
        self.assertEqual(1, 1)

    @given(strategies.integers(), strategies.integers())
    def test_build_tree(self, a, b):
        expression = "a + 2 - b"
        interpreter = ExpressionTreeInterpreter()
        tree = interpreter.build_expression_tree(expression)
        variable_values = {'a': a, 'b': b}
        result = interpreter.evaluate(tree, variable_values)
        self.assertEqual(result, a + 2 - b)

    def test_evaluate(self):
        self.assertEqual(1, 1)

    def test_visualize(self):
        self.assertEqual(1, 1)
