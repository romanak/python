# Write your code here :-)
# Asks user to enter 10 integers and outputs the largest odd integer

data = [0]
while len(data) != 10:
    rawdata = input("Enter 10 integers separated by space:")
    data = rawdata.split(" ")
odd = None
for d in data:
    d = int(d)
    if (d%2 != 0) and (odd == None or d > odd):
        odd = d
if odd != None:
    print("The largest odd number:",odd)
else:
    print("No odd number was entered!")
print(data)