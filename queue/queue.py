class Queue:
  class LinkedNode:
    def __init__(self, element, next):
      self.next = next
      self.element = element

  def __init__(self):
    self.__size = 0
    self.__first = self.LinkedNode(None, None)
    self.__last = self.__first

  def count(self):
    return self.__size

  def isEmpty(self):
    return self.__size == 0

  def peek(self):
    if self.isEmpty():
      raise Exception("[Error] Can't peek an empty queue.")
    return self.__first.next.element

  def enqueue(self, element):
    if element == None:
      raise Exception("[Error] Node's element can't be null.")
    newElement = self.LinkedNode(element, None)
    self.__last.next = newElement
    self.__last = newElement
    self.__size += 1

  def dequeue(self):
    if self.__first.next == None:
      raise Exception("[Error] Can't dequeue from an empty queue.")
    node = self.__first.next
    self.__first.next = node.next
    self.__size -= 1
    if node.next == None:
      self.__last = self.__first
    return node.element
    
  # def traverse(self):
  #   if self.__size > 0:
  #     current = self.__first
  #     while current.next:
  #       print(current.next.element)
  #       current = current.next
  #   else:
  #     print("Empty queue")