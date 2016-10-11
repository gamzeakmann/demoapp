import unittest
from algorithm import search

class TestSearch(unittest.TestCase):
  def setUp(self):
    self.array = [10, 20, 30, 40, 50, 60]

  def test_successful(self):
    self.assertTrue(search(self.array, 10, 20))

  def test_failed(self):
    self.assertFalse(search(self.array, 60, 60))

  def test_emptyArray(self):
    self.assertFalse(search([], 10, 40))

  def test_searchingNegativeNumberInPositiveArray(self):
    self.assertFalse(search(self.array, -10, -30))

  def test_searchingNoneSuccessful(self):
    self.assertFalse(search([None], 10, 20))


if __name__ == '__main__':
    unittest.main()
