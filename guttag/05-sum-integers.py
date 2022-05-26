#Prints the sum of integers in a string_to_bytes
s = input('Enter decimal numbers separated by commas: ')
data = s.split(',')
sum = 0
for d in data:
    sum += float(d)
print('Sum of numbers is',sum)