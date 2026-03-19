import unittest
from dab.account import *

class DABUnitTests(unittest.TestCase):
  def test_checkWithdrawal(self):
    self.assertEqual(checkWithdrawal(1000,1), True)
    self.assertEqual(checkWithdrawal(1000,600), False)
    self.assertEqual(checkWithdrawal(1000,5000000000), False)
    self.assertEqual(checkWithdrawal(1000,-1), False)
    

if __name__ == '__main__':
  unittest.main()
