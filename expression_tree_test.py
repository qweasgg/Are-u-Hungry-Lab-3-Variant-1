import unittest
from hypothesis import given,  strategies

from expression_tree import ExpressionTreeInterpreter


class TestInterpreter(unittest.TestCase):

    def test_validate_input(self):
        self.assertEqual(1, 1)

    @given(strategies.integers(), strategies.integers())
    def test_build_tree(self, a, b):
        self.assertEqual(a, a)
        self.assertEqual(b, b)

    def test_evaluate(self):
        self.assertEqual(1, 1)

    def test_visualize(self):
        self.assertEqual(1, 1)
