def calculateCreditCardBalance(balance,annualInterestRate,monthlyPaymentRate):
'''
calculate the credit card balance after one year if a person only pays the minimum 
monthly payment required by the credit card company each month
'''
    prevBalance = balance
    totalPayment = 0
    for month in range(1,13):
        monthlyInterestRate = annualInterestRate/12.0
        minimumMonthlyPayment = monthlyPaymentRate * prevBalance
        monthlyUnpaidBalance = prevBalance - minimumMonthlyPayment
        prevBalance = monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
        totalPayment += minimumMonthlyPayment
        print "Month: ",month
        print "Minimum monthly payment: " , round(minimumMonthlyPayment,2)
        print "Remaining balance: ", round(prevBalance,2)

    print "Total paid: ", round(totalPayment,2)
    print "Remaining balance: ", round(prevBalance,2)


calculateCreditCardBalance(balance,annualInterestRate,monthlyPaymentRate)
