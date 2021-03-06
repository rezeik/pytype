"""Tests for abc_hierarchy.py."""

import unittest
from pytype.pytd import abc_hierarchy


class TestAbcHierarchy(unittest.TestCase):
  """Test abc_hierarchy.py."""

  def testGetSuperClasses(self):
    superclasses = abc_hierarchy.GetSuperClasses()
    self.assertDictEqual(superclasses, abc_hierarchy.SUPERCLASSES)
    # Verify that we made a copy.
    self.assertIsNot(superclasses, abc_hierarchy.SUPERCLASSES)

  def testGetSubClasses(self):
    subclasses = abc_hierarchy.GetSubClasses()
    # Check one entry.
    self.assertSetEqual(
        set(subclasses['Sized']), {'Set', 'Mapping', 'MappingView', 'Sequence'})


if __name__ == '__main__':
  unittest.main()
