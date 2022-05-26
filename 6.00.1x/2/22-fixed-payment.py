balance = 3926
annualInterestRate = 0.2
payment = 0
testbalance = balance
while testbalance > 0:
    testbalance = balance
    payment += 0.01
    for month in range(12):
        testbalance = testbalance - payment
        testbalance = testbalance*(1+annualInterestRate/12)
print('Lowest Payment:', payment)