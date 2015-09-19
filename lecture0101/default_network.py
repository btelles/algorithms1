class DefaultNetwork(object):
  def __init__(self):
    self.network = {}

  def connected(self, int_a, int_b):
    raise Exception("Not Implemented")

  def union(self, int_a, int_b):
    raise Exception("Not Implemented")

  def show(self):
    for k, v in self.network.items():
      self._print_root(k, v, '')

  def _print_root(self, origin, destination, route, count=0):
    if (not route):
      route = "%s" % origin

    print("c: %s, r: %s, o: %s, d: %s" % (count, route, origin, destination))
    count += 1
    if((not origin == destination) and (count < 5 ) ):
      route += (" -> %i" % destination)
      self._print_root(destination, self.network[destination], route, count)
    else:
      print(route)
