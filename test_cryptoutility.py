# test_cryptoutility.py
"""
Tests for CryptoUtility module.
"""

import unittest
from cryptoutility import CryptoUtility

class TestCryptoUtility(unittest.TestCase):
    """Test cases for CryptoUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoUtility()
        self.assertIsInstance(instance, CryptoUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
