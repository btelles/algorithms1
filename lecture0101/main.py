import default_network

class QuickFindUF(default_network.DefaultNetwork):

  def connected(self, int_a, int_b):
    try:
      return self.network[int_a] == self.network[int_b]
    except KeyError:
      return False

  def union(self, int_a, int_b):
    self.network.setdefault(int_a, int_a)
    self.network.setdefault(int_b, int_b)
    for key, value in self.network.items():
      self.show()
      if(value in (self.network[int_a], self.network[int_b])):
        print("Value found.")
        self.network[key] = int_a


uf = QuickFindUF()

get_pair = True

while(True):
  user_input = input("Enter two integers: ")
  two_ints = user_input.split(" ")

  try:
    int_a, int_b = map(int, two_ints)
  except:
    print("All done.")
    break

  if(not uf.connected(int_a, int_b)):
    uf.union(int_a, int_b)
    print("Newly connected: %s, %s" % (int_a, int_b))
    print("New network is: %s" % uf.network)


