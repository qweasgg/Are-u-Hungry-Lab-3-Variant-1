import unittest
from expression_tree import ExpressionTreeInterpreter


class TestInterpreter(unittest.TestCase):

    def test_evaluate(self):
        user_function = {'foo': lambda x, y, z: x / y + z}
        interpreter = ExpressionTreeInterpreter(user_function)
        expression1 = '1 + 1'
        variable_values1 = {}
        interpreter.prase_expression(expression1, variable_values1)
        self.assertEqual(interpreter.result, 2)
        expression2 = 'a + 1'
        variable_values2 = {'a': 2}
        interpreter.prase_expression(expression2, variable_values2)
        self.assertEqual(interpreter.result, 3)
        expression3 = 'foo(2, 1, 0) + 1'
        variable_values3 = {}
        interpreter.prase_expression(expression3, variable_values3)
        self.assertEqual(interpreter.result, 3)
        expression4 = "sin(-30)*(a + 2) - foo(b, c, d)*(2 - 1)"
        variable_values4 = {'a': 1, 'b': 3, 'c': 2, 'd': 1}
        interpreter.prase_expression(expression4, variable_values4)
        self.assertEqual(interpreter.result, -4)

    def test_validate_input(self):
        interpreter = ExpressionTreeInterpreter()
        with self.assertRaises(ValueError):
            interpreter.build_expression_tree("")  # empty input
        with self.assertRaises(ValueError):
            interpreter.build_expression_tree("a + * 2")   # Invalid exp
        tree = interpreter.build_expression_tree("a + 2")
        with self.assertRaises(RuntimeError) as cm:
            interpreter.evaluate(tree, {'b': 2})
            self.assertEqual(
                            str(cm.exception),
                            "Name error: Variable 'a' is not defined.")
