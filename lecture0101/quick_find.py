import default_network

class QuickFindUF(default_network.DefaultNetwork):

  def connected(self, int_a, int_b):
    if(int_a == int_b):
      return True
    try:
      return self.network[int_a] == self.network[int_b]
    except KeyError:
      return False

  def union(self, int_a, int_b):
    self.network.setdefault(int_a, int_a)
    self.network.setdefault(int_b, int_b)
    root_a = self.network[int_a]
    root_b = self.network[int_b]
    for key, value in self.network.items():
      if(value in (root_a, root_b)):
        self.network[key] = root_a
