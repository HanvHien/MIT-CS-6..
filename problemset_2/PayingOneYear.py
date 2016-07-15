#         test case
balance = 4773
annualInterestRate = 0.2
#######################################

previous_Balance = balance
fixedMonthlyPayment = round(balance / 120.0) * 10
MonthlyInterest = (annualInterestRate) / 12.0
TotalPaid = 0

previous_Balance = balance
paid_enough = False
while not paid_enough:

    for m in range(12):
        Monthly_unpaid_balance = previous_Balance - fixedMonthlyPayment
            
        updated_Bal_each_month = Monthly_unpaid_balance + (MonthlyInterest * Monthly_unpaid_balance)

        previous_Balance = updated_Bal_each_month
        TotalPaid += fixedMonthlyPayment

    if (previous_Balance<=0):
        paid_enough = True
    else:      
        fixedMonthlyPayment += 10
        previous_Balance = balance
        TotalPaid = 0
print 'Lowest Payment: {:}'.format(int(fixedMonthlyPayment))
