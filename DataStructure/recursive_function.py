# class Node():
#   def __init__():
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
    node = None
    new_node = Node(data)
    self.size += 1

    if self.header == None:
      self.header = new_node

    else:


  def print_list(self):
    print("------")
    node = self.header

    while node != None:
      print(node.get_data())
      node = self.header.get_next()
    print("------")

sll = Simply_Linked_list()

sll.append("Tiger")
sll.append("Duck")
sll.append("Dog")
sll.print_list() 
      

    
  