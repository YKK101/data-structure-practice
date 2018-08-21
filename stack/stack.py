class Stack:
  def __init__(self):
    self.__size = 0
    self.__list = []
  
  def count(self):
    return self.__size

  def peek(self):
    if self.__size == 0:
      raise Exception("[Error] Can't peek an empty stack.")
    return self.__list[self.__size - 1]

  def push(self, data):
    if data == None:
      raise Exception("[Error] Stack data can't be null.")
    self.__list.append(data)
    self.__size += 1
  
  def pop(self):
    if self.__size == 0:
      raise Exception("[Error] Can't pop anything from an empty stack.")
    self.__size -= 1
    data = self.__list[self.__size]
    del self.__list[self.__size]
    return data