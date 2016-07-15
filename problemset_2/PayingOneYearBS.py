
#         test case
balance = 999999
annualInterestRate = 0.18
#######################################


def evalPay(payment):
    previous_Balance = balance

    for m in range(12):
        Monthly_unpaid_balance = previous_Balance - payment

        updated_Bal_each_month = Monthly_unpaid_balance + (MonthlyInterest * Monthly_unpaid_balance)

        previous_Balance = updated_Bal_each_month
    return round(previous_Balance, 2)


MonthlyInterest = (annualInterestRate) / 12.0

# initializing MinPay , Maxpay
MinPay = balance / 12
MaxPay = (balance * (1 + MonthlyInterest)**12) / 12.0

paid_enough = False
while not paid_enough:

    midpoint = 0.5 * (MinPay + MaxPay)

    fixedMonthlyPayment = midpoint
    p = evalPay(fixedMonthlyPayment)
    if p > 0:
        MinPay = midpoint
    elif p < 0:
        MaxPay = midpoint
    else:
        paid_enough = True


print 'Lowest Payment: {:.2f}'.format(fixedMonthlyPayment)

