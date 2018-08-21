from stack import Stack

def isOpenPharenthesis(character):
  return character == "(" or character == "[" or character == "{"

def isCorrectClosedType(openChar, closeChar):
  return openChar == "(" and closeChar == ")" \
      or openChar == "[" and closeChar == "]" \
      or openChar == "{" and closeChar == "}"

def checkPharenthesis(question):
  ans = True
  stack = Stack()

  for character in question:
    if isOpenPharenthesis(character):
      stack.push(character)
    else:
      try:
        lastOpen = stack.pop()
        if not isCorrectClosedType(lastOpen, character):
          raise Exception("[Error] Wrong close pharenthesis type.")
      except Exception:
        print("%s is in wrong format!" % question)
        ans = False
        break

  if stack.count() > 0:
    ans = False
    print("%s is in wrong format!" % question)

  if ans:
    print("%s format is correct!" % question)


question = ""
while not question == "end":
  question = raw_input("Please insert your question:\n")
  checkPharenthesis(question)