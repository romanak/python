import matplotlib.pylab as plt

class Mortgage(object):
    """
    Abstract class for building various kinds of mortgages
    (principal) loan principal
    (annualRate) annual interest rate
    (duration) duration of the morgage in months
    """
    def __init__(self, principal, annualRate, duration):
        self.rincipal = principal
        self.annualRate = annualRate
        self.rate = annualRate/12
        self.duration = duration
        self.paid = [0.0]
        self.owed = [principal]
        self.payment = self.monthlyPayment(principal, annualRate/12, duration)
        self.legend = None
    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    def getTotalPaid(self):
        return sum(self.paid)
    def monthlyPayment(self, principal, rate, duration):
        """
        Assumes: (principal) and (rate) are floats, (duration) is an integer
        Returns the monthly payment for a fixed rate mortgage
        """
        if rate == 0:
            return principal/duration
        else:
            return (rate*principal)/(1-(1+rate)**(-duration))
    def getTotalInterest(self):
        return getTotalPaid() - self.principal
    def __str__(self):
        return self.legend
    def plotPayment(self):
        plt.figure('Payments')
        plt.xlabel('Months')
        plt.ylabel('Amount in U.S. dollars')
        plt.title('Payments')
        plt.plot(self.paid[1:], label = self.legend, linewidth = 1.0)
        plt.legend(loc = 'best')
    def plotMortgage(self):
        totPaid = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPaid.append(totPaid[-1] + self.paid[i])

        plt.figure(self.legend)
        plt.clf()
        plt.xlabel('Months')
        plt.ylabel('Amount in U.S. dollars')
        plt.title(self.legend)
        plt.plot(self.owed, 'b-', label = 'owed', linewidth = 1.0)
        plt.plot(totPaid, 'r-', label = 'paid', linewidth = 1.0)
        plt.legend(loc = 'best')
        self.plotPayment()

class Fixed(Mortgage):
    def __init__(self, principal, annualRate, duration):
        Mortgage.__init__(self, principal, annualRate, duration)
        self.legend = 'Fixed, ' + str(round(self.annualRate*100, 2)) + '%'

class Teaser(Mortgage):
    def __init__(self, principal, annualRate, duration, teaserRate, teaserDuration):
        Mortgage.__init__(self, principal, annualRate, duration)
        self.teaserRate = teaserRate
        self.teaserDuration = teaserDuration
        self.rate = teaserRate/12
        self.nextRate = annualRate/12
        self.payment = self.monthlyPayment(principal, teaserRate/12, duration)
        self.legend = 'Teaser, ' + str(round(self.teaserRate*100, 2)) + '% for ' + str(self.teaserDuration) + ' months, then ' + str(round(self.annualRate*100, 2)) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserDuration + 1:
            self.rate = self.nextRate
            self.payment = self.monthlyPayment(self.owed[-1], self.rate, self.duration - self.teaserDuration)
        Mortgage.makePayment(self)

def compareMortgages(principal, annualRate, years, teaserRate, teaserDuration):
    duration = years*12
    fixed = Fixed(principal, annualRate, duration)
    teaser = Teaser(principal, annualRate, duration, teaserRate, teaserDuration)
    mortgages = [fixed, teaser]
    for m in range(duration):
        for mortgage in mortgages:
            mortgage.makePayment()
    for mortgage in mortgages:
        print(mortgage.legend + ' Total payments = $' + str(round(mortgage.getTotalPaid(),2)))
        mortgage.plotMortgage()
    plt.show()

compareMortgages(300000, 0.05, 30, 0.03, 12)