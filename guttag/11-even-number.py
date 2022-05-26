def findAnEven(l):
  """Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number"""
  even = None
  for i in l:
    if i%2 == 0:
      even = i
      break
  if even == None:
    raise ValueError('No even number found')
  return even

print(findAnEven([1,3,3,7,5]))