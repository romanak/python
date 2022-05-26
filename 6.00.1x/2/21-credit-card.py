balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
    balance = balance - balance*monthlyPaymentRate
    balance = balance*(1 + annualInterestRate/12)
print('Remaining balance:', round(balance, 2))