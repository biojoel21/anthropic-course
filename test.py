"""
Test file for the calculate_pi function in main.py
"""
import unittest
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_5_digits(self):
        """Test that pi is calculated correctly to 5 decimal digits"""
        result = calculate_pi(5)
        expected = 3.14159  # Pi to 5 decimal places
        
        # Check that result matches to 5 decimal places
        self.assertAlmostEqual(result, expected, places=5,
                              msg=f"Expected {expected}, but got {result}")
    
    def test_pi_default(self):
        """Test that default parameter works correctly"""
        result = calculate_pi()
        expected = 3.14159
        
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_pi_more_digits(self):
        """Test calculation with more digits for accuracy"""
        result = calculate_pi(10)
        expected = 3.1415926536  # Pi to 10 decimal places
        
        self.assertAlmostEqual(result, expected, places=10,
                              msg=f"Expected {expected}, but got {result}")
    
    def test_pi_value_in_range(self):
        """Test that pi is within reasonable bounds"""
        result = calculate_pi(5)
        
        # Pi should be between 3.14159 and 3.14160
        self.assertGreater(result, 3.14159)
        self.assertLess(result, 3.14160)
    
    def test_pi_first_digits(self):
        """Test the first 5 digits after decimal point"""
        result = calculate_pi(5)
        result_str = f"{result:.5f}"
        
        self.assertEqual(result_str, "3.14159",
                        msg=f"Expected '3.14159', but got '{result_str}'")


def manual_test():
    """Manual test to visually inspect the output"""
    print("=" * 50)
    print("Manual Test Results for calculate_pi()")
    print("=" * 50)
    
    print(f"\nPi to 5 digits: {calculate_pi(5):.5f}")
    print(f"Expected value:  3.14159")
    
    print(f"\nPi to 10 digits: {calculate_pi(10):.10f}")
    print(f"Expected value:   3.1415926536")
    
    print(f"\nPi to 15 digits: {calculate_pi(15):.15f}")
    print(f"Expected value:   3.141592653589793")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    # Run manual test first
    manual_test()
    
    # Run unit tests
    print("\nRunning unit tests...\n")
    unittest.main(verbosity=2)
