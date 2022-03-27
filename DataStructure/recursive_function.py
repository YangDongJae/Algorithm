class Node():
  def __init__(self,data):
    self.node = data
    self.next = None

  def get_data(self):
    return self.node

  def get_next(self):
    return self.next

  def set_next(self,data):
    self.next = data


class Simply_Linked_list():
  def __init__(self):
    self.header = None
    self.size = 0

  def append(self,data):
    new_node = Node(data)
    self.size += 1

    if self.header == None:
      self.header = new_node

    else:
      node = self.header
      while node.get_next() != None:
        node = node.get_next()
        break
      node.set_next(new_node)
        

  def print_list(self):
    print("------")
    node = self.header

    while node != None:
      print(node.get_data())
      node = node.get_next()
    print("------")

sll = Simply_Linked_list()

sll.append("Tiger")
sll.append("Duck")
sll.append("Dog")

sll.print_list()
      

    
  