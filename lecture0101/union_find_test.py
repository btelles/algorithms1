import unittest
from nose_parameterized import parameterized
import quick_find
import quick_union_find
import weighted_quick_union_find

class QuickFindUFTest(unittest.TestCase):
  classes = [(quick_find.QuickFindUF,),
             (quick_union_find.QuickUnionFindUF,),
             (weighted_quick_union_find.WeightedQuickUnionFindUF,)]

  @parameterized.expand(classes)
  def test_empty_network_only_has_base_connections(self, class_to_test):
    qf = class_to_test()
    self.assertFalse(qf.connected(0, 1))
    self.assertFalse(qf.connected(1, 2))
    self.assertTrue(qf.connected(1, 1))

  @parameterized.expand(classes)
  def test_unioning_two_things_causes_them_to_connect(self, class_to_test):
    qf = class_to_test()
    self.assertFalse(qf.connected(1, 2))
    qf.union(1, 2)
    self.assertTrue(qf.connected(1, 2))

  @parameterized.expand(classes)
  def test_unioning_two_distant_things_causes_them_to_connect(self, class_to_test):
    qf = class_to_test()
    self.assertFalse(qf.connected(1, 3))
    qf.union(1, 2)
    qf.union(2, 3)
    self.assertTrue(qf.connected(1, 3))

  @parameterized.expand(classes)
  def test_unioning_two_distant_things_in_reverse_order(self, class_to_test):
    qf = class_to_test()
    self.assertFalse(qf.connected(2, 4))
    qf.union(1, 2)
    qf.union(3, 4)
    qf.union(4, 1)
    self.assertTrue(qf.connected(2, 4))

if(__name__ == '__main__'):
  unittest.main()
