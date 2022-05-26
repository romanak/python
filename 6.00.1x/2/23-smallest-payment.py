balance = 157540
annualInterestRate = 0.22

low = balance/12
high = balance*(1+annualInterestRate)/12
testbalance = balance

while abs(testbalance) > 0.01:
    testbalance = balance
    payment = (low+high)/2
    for month in range(12):
        testbalance = testbalance - payment
        testbalance = testbalance*(1+annualInterestRate/12)
    if testbalance > 0:
        low = payment
    else:
        high = payment
print('Lowest Payment:', round(payment,2))