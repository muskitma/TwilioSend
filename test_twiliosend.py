# test_twiliosend.py
"""
Tests for TwilioSend module.
"""

import unittest
from twiliosend import TwilioSend

class TestTwilioSend(unittest.TestCase):
    """Test cases for TwilioSend class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TwilioSend()
        self.assertIsInstance(instance, TwilioSend)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TwilioSend()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
