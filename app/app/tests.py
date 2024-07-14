
"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers togather."""
        res = calc.add(5, 6)
    
        self.assertEqual(res, 11)
        print("The result is: " + str(res))

print("Test is done. Thanks")
