# Author: Conor Smith
# Date: 4/28/21
# Description: multiplies two numbers together by using adding and recursion

def multiply(n, m):
  """This is a function that takes two numbers and multiplys them by adding the first number to itself, the second number amount of times"""

  if m == 0:
    return 0
  if m < 2:
    return n
  return n + multiply(m-1, n)