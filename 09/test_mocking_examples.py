import math
import unittest
from unittest import mock


def function_under_test(arg):
    return math.cos(arg)

def fake_cos(arg):
    return 'fake!!!!'

class MockExamples(unittest.TestCase):

    @mock.patch('math.cos')
    def test_basic_mock(self, mock_cos):
        mock_cos.return_value = 'my mock value'
        self.assertEqual(function_under_test(123), 'my mock value')
    
    @mock.patch('math.cos')
    def test_validate_mock_calls(self, mock_cos):
        mock_cos.return_value = 'my mock value'
        function_under_test(123)
        mock_cos.assert_called_with(123)
    
    @mock.patch('math.cos')
    def test_mock_with_error(self, mock_cos):
        mock_cos.side_effect = ValueError
        with self.assertRaises(ValueError):
            function_under_test(123)
    
    @mock.patch('math.cos', wraps=fake_cos)
    def test_mock_with_fake_impl(self, mock_cos):
        self.assertEqual(function_under_test(123), 'fake!!!!')

    def test_mock_defined_in_testcase(self):
        def nested_fake_cos(arg):
            self.assertEqual(arg, 123)
            return 'nested fn'
        with mock.patch('math.cos', wraps=nested_fake_cos) as mock_cos:
            self.assertEqual(function_under_test(123), 'nested fn')


if __name__ == '__main__':
    unittest.main()
