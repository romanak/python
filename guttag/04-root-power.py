#Asks for an integer num and prints 0 < pwr < 6 and root such that root**pwr=num
num = int(input('Enter an integer: '))
ans = False
pwr = 1
while pwr < 6:
    root = 0
    while root <= abs(num):
        if (root**pwr == abs(num)) and (num >= 0 or pwr%2 != 0):
            if num < 0:
                print(str(-root)+'^'+str(pwr)+'='+str(num))
            else:
                print(str(root)+'^'+str(pwr)+'='+str(num))
            ans = True
        root += 1
    pwr += 1
if not ans:
    print('No such pair of integers exists!')