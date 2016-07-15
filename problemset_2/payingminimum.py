#         test case
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#######################################

previousBalance = balance
MonthlyInterest = (annualInterestRate) / 12.0
TotalPaid = 0

for m in range(12):
    minMonthlyPayment = monthlyPaymentRate * previousBalance
    Monthly_unpaid_balance = previousBalance - minMonthlyPayment
    updated_Bal_each_month = Monthly_unpaid_balance + (MonthlyInterest * Monthly_unpaid_balance)

    print 'Month: {:}'.format(m + 1)
    print 'Minimum monthly payment: {:.2f}'.format(minMonthlyPayment)
    print 'Remaining balance: {:.2f}'.format(updated_Bal_each_month)
    previousBalance = updated_Bal_each_month
    TotalPaid += minMonthlyPayment
print 'Total paid: {:.2f}'.format(TotalPaid)
print 'Remaining balance: {:.2f}'.format(updated_Bal_each_month)
