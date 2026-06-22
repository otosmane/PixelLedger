# test_pixelledger.py
"""
Tests for PixelLedger module.
"""

import unittest
from pixelledger import PixelLedger

class TestPixelLedger(unittest.TestCase):
    """Test cases for PixelLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelLedger()
        self.assertIsInstance(instance, PixelLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
