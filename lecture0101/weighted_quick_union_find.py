import quick_union_find

class WeightedQuickUnionFindUF(quick_union_find.QuickUnionFindUF):
  def __init__(self):
    super().__init__()
    self.size = {}

  def union(self, int_a, int_b):
    if(not self.connected(int_a, int_b)):
      root_a = self._root(int_a)
      root_b = self._root(int_b)
      if(self.size.setdefault(root_a, 1) > self.size.setdefault(root_b, 1)):
        self.network[root_b] = self.network[root_a]
        self.size[root_b] += self.size[root_a]
      else:
        self.network[root_a] = self.network[root_b]
        self.size[root_a] += self.size[root_b]
