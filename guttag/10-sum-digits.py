def sumDigits(s):
  """Assumes s is a string
    Returns the sum of the decimal digits ins
      For example, if s is 'a2b3c' it returns 5"""
  sd = 0
  for c in s:
    try:
      sd += int(c)
    except:
      continue
  return sd

print(sumDigits('a2b3c1tre.4th1'))