import default_network

class QuickUnionFindUF(default_network.DefaultNetwork):

  def connected(self, int_a, int_b):
    return self._root(int_a) == self._root(int_b)

  def union(self, int_a, int_b):
    if(not self.connected(int_a, int_b)):
      root_a = self._root(int_a)
      root_b = self._root(int_b)
      self.network[root_a] = self.network[root_b]

  def _root(self, int_a):
    possible_root = int_a
    while(not self.network.setdefault(possible_root, int_a) == possible_root):
      possible_root = self.network[possible_root]
    return possible_root
