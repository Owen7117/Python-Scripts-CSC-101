#program 8 Basic: Credit Card Debt Revisited
#Owen O'Neil
#3/29/24

def credit_card_debt_payment(balance, interest_rate, monthly_payment, months=0):
    interest = balance * (interest_rate/12)#interest in money to compare to montly payment
    if balance <= 0:#balance owed is 0 or less 
        return ("It takes {} months to pay of your credit card debt".format(months))
    elif interest >= monthly_payment:#You are paying less than the interest requires so you will nevery pay it off 
        return ("You will never pay off your credit card debt with this monthly payment")   
    else:
        balance += interest#interest added to balance
        balance -= monthly_payment#decreases balance owed by montly payment
        return credit_card_debt_payment(balance, interest_rate, monthly_payment, months+1)#adds one to month count when recursion is called 
      

balance = float(input("Outstanding balance on your credit card: "))
interest_rate = float(input("Annual interest rate (as a decimal): "))
monthly_payment = float(input("Minimum monthly payment: "))

print(credit_card_debt_payment(balance, interest_rate, monthly_payment))#call subroutine 



